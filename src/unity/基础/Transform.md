# Transform



Transform是unity里面的转换组件，负责层级，位置，旋转，还有一些局部坐标、世界坐标之间的转换



## TransformPoint

```c#
public Vector3 TransformPoint(Vector3 position)
{
    TransformPoint_Injected(ref position, out Vector3 ret);
    return ret;
}
```

目的是把一个坐标点从局部坐标系转换到世界坐标系



实现原理：

```c++
inline math::float3 TransformPoint(TransformAccessReadOnly transformAccess, const math::float3& point)
{
    ASSERT_TRANSFORM_ACCESS(transformAccess);

    using namespace math;

    math::float3 p = point;

    const trsX* localTransforms = transformAccess.hierarchy->localTransforms;

    SInt32 *parentIndices = transformAccess.hierarchy->parentIndices;
    SInt32 parentIndex = transformAccess.index;

    while (parentIndex >= 0)
    {
        p = mul(localTransforms[parentIndex], p);
        parentIndex = parentIndices[parentIndex];
    }

    return p;
}
```

```c++
    static MATH_FORCEINLINE float3 mul(trsX const& x, float3 const& v)
    {
        return x.t + quatMulVec(x.q, v * x.s);//先进行缩放，再进行四元数旋转，再加偏移计算
    }
```



先取当前的localTransforms，依次获取父级的localTransform，乘于点p，得到在该父级坐标系下的坐标点p，这样依次迭代，直到没有了父级，即转换到了世界坐标系。



## InverseTransformPoint

```c#
        public Vector3 InverseTransformPoint(Vector3 position)
        {
            InverseTransformPoint_Injected(ref position, out Vector3 ret);
            return ret;
        }
```

目的是将世界坐标点从世界坐标系转换到局部坐标系



实现原理：

```c++
inline void InverseTransformPosition(TransformAccessReadOnly transformAccess, math::float3& p)
{
    ASSERT_TRANSFORM_ACCESS(transformAccess);

    using namespace math;

    if (transformAccess.index > 0)
        InverseTransformPosition(GetParent(transformAccess), p);

    const trsX &trs = GetLocalTRS(transformAccess);
    p = invMul(trs, p);
}
```

递归调用InverseTransformPosition，即将点从世界坐标转换到最顶层的父级，再依次转换到当前的局部坐标系。

```c++
    static MATH_FORCEINLINE float3 invMul(trsX const& x, float3 const& v)
    {
        //先做偏移，再反转旋转，再反转缩放
        return quatMulVec(quatConj(x.q), v - x.t) * inverseScale(x.s);
    }
```

```c++
    // returns the inverse of q.
    // * if q is normalized. The inverse quaternions is also normalized
    // * it is legal to call quatConj with non-normalized quaternion, the output will also be non-normalized
    static MATH_FORCEINLINE float4 quatConj(const float4& q)
    {
        //@TODO: If we switch to quaternion type instead of float4 type
        //       then we could rename this to inverse
        return chgsign(q, float4(-1.f, -1.f, -1.f, 1.f));
    }
```



## forward

设置朝向

```c#
        //
        // 摘要:
        //     ///
        //     Returns a normalized vector representing the blue axis of the transform in world
        //     space.
        //     ///
        public Vector3 forward
        {
            get
            {
                return rotation * Vector3.forward;
            }
            set
            {
                rotation = Quaternion.LookRotation(value);
            }
        }
```

即转为一个四元数旋转来表达朝向

原理：

```c#
        //
        // 摘要:
        //     ///
        //     Creates a rotation with the specified forward and upwards directions.
        //     ///
        //
        // 参数:
        //   forward:
        //     The direction to look in.
        //
        //   upwards:
        //     The vector that defines in which direction up is.
        [ExcludeFromDocs]
        public static Quaternion LookRotation(Vector3 forward)
        {
            return LookRotation(forward, Vector3.up);
        }
```



朝向和一个世界坐标的up向量，决定一个四元数旋转

```c++
inline Quaternionf QuaternionScripting::LookRotation(const Vector3f& forward, const Vector3f& upwards)
{
    Quaternionf q = Quaternionf::identity();
    if (!LookRotationToQuaternion(forward, upwards, &q))
    {
        const float mag = Magnitude(forward);
        if (mag > Vector3f::epsilon)
        {
            //这里如果与up向量构造旋转失败，则用z向量与朝向进行构造
            Matrix3x3f m; m.SetFromToRotation(Vector3f::zAxis, forward / mag);
            MatrixToQuaternion(m, q);
        }
        else
        {
            LogString("Look rotation viewing vector is zero");
        }
    }
    return q;
}
```

```c++
bool LookRotationToQuaternion(const Vector3f& viewVec, const Vector3f& upVec, Quaternionf* res)
{
    Matrix3x3f m;
    if (!LookRotationToMatrix(viewVec, upVec, &m))//得到3x3旋转矩阵
        return false;
    MatrixToQuaternion(m, *res);//3x3旋转矩阵转为四元数
    return true;
}
```

```c++
// Right handed
bool LookRotationToMatrix(const Vector3f& viewVec, const Vector3f& upVec, Matrix3x3f* m)
{
    Vector3f z = viewVec;
    // compute u0
    float mag = Magnitude(z);
    if (mag < Vector3f::epsilon)
    {
        m->SetIdentity();
        return false;
    }
    z /= mag;//朝向为z轴

    Vector3f x = Cross(upVec, z);//up向量旋转到z的叉积，即为x轴向量
    mag = Magnitude(x);
    if (mag < Vector3f::epsilon)
    {
        m->SetIdentity();
        return false;//
    }
    x /= mag;

    Vector3f y(Cross(z, x));//z轴和x轴叉积即为y轴向量
    if (!CompareApproximately(SqrMagnitude(y), 1.0F))
        return false;//如果朝向与x几乎平行，返回false

    m->SetBasis(x, y, z);
    return true;
}
```



从代码实现的原理看：朝向会先默认up向量，通过叉积找到x向量，再通过朝向与x向量叉积找到y向量，如果构造失败，则用世界z向量与朝向来进行构造，得到四元数旋转后，设置到transform的rotation变量中。