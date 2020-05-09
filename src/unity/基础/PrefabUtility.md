# PrefabUtility

## 创建一个空prefab

函数原型如下：
```c#
public static Object CreateEmptyPrefab(string path)
```
该函数先创建一个空的GameObject对象

然后再调用SaveAsPrefabAsset对该GameObject对象序列化到所传路径

再立即删除空的GameObject对象

返回序列化的prefab对象



## 另存为PrefabAsset

函数原型如下：
```c#
public static GameObject SaveAsPrefabAsset(GameObject instanceRoot, string assetPath, out bool success)
```
此函数调用SaveAsPrefabAsset_Internal c++实现

```c#
    [StaticAccessor("PrefabUtilityBindings", StaticAccessorType.DoubleColon)]
    extern private static GameObject SaveAsPrefabAsset_Internal([NotNull] GameObject root, string path, out bool success);
```

实体化Prefab

```c#
public static Object InstantiatePrefab(Object assetComponentOrGameObject)
public static Object InstantiatePrefab(Object assetComponentOrGameObject, Scene destinationScene)
public static Object InstantiatePrefab(Object assetComponentOrGameObject, Transform parent)
```



应用Prefab实例
函数原型如下：

```c#
internal static void ApplyPrefabInstance(GameObject instance)
```
此函数在经过一些相关检测后，最终会调用ApplyPrefabInstance_Internal c++实现
```c#
        [StaticAccessor("PrefabUtilityBindings", StaticAccessorType.DoubleColon)]
        extern private static GameObject ApplyPrefabInstance_Internal([NotNull] GameObject root);
```



回滚Prefab实例

主要目的是回滚Prefab实例的修改，保持与Prefab一样

函数原型如下：

```c#
public static void RevertPrefabInstance(GameObject instanceRoot, InteractionMode action)
```

