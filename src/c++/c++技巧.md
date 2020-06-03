# C++技巧

## 1.通过类成员数据地址获取对象地址

```c++
typedef struct element_s {
	struct element_s* next;
	int              t;
} element_t;//结构体定义
```

```c++
element_t* e = new element_t;
e->next = nullptr;
e->t = 100;
int* value = &(e->t);

//这里value指向结构体里面的值
element_t* e2 = (element_t*)(((unsigned char*)value) - ((int)&((element_t*)0)->t));
//((unsigned char*)value) 转换为字节指针
//((element_t*)0),把0转换为element_t*型的指针
//((element_t*)0)->t,是指向值t
//&((element_t*)0)->t,是取t的地址
//(int)&((element_t*)0)->t,将t的地址转换为整形int，这里因为对象基地址是0，所以t的地址就是相对基地址
//的偏移，此例中，如果是64位程序，则偏移是8个字节的偏移，如果32位程序，则是4个字节的偏移。
//当传入的value这样其他对象数据地址的时候，可以将该地址减去偏移，就是对象地址了。
//可以验证这里e2的地址和e是一样的。
```





