# Unreal4 Problem

1.蓝图机制原理

2.蓝图编译

3.网络同步模块，是如何进行网络同步的

4.delegate实现原理

5.TShareFromThis原理，

6.class FUniqueNetId : public TSharedFromThis<FUniqueNetId>

7.UE4 容器用法

8.UStruct为什么不能用指针

9.枚举为什么要写成TEnumAsByte

10.buff免疫检查（遍历所有buff，检查一遍，有点耗？）

11.buff互斥遍历（有点耗？）

12.buff叠加攻击者，就不叠加层数了？

13.TSharedFromThis, TSharedPtr,  TWeakPtr, TSharedRef,  FWeakReferencer,  FSharedReferencer, FReferenceControllerBase, FRawPtrProxy,TSoftObjectPtr



14.SharedReferenceCount计数是用来删除对象的，WeakReferenceCount计数是用来删除ReferenceController（引用控制器）

15.300-2000范围的概率

16.FString与FName区别



17. EventInitFromSkill是哪里调用的？OnSkillCustomEvent是怎样发送到SkillActor里的
18. UTSkillPhase里面ForceStopPhase 是为何调用两次Action的Resset
19. UTSkillPhase 对于SPT_Repeat，有可能出现RepeatPhase和StopPhase计时器，但是ForceStopPhase里面，针对SPT_Repeat只清除了RepeatPhase计时器
20. UE4 dll热加载
21. 插件模块
22. EndPlay是哪时候调用的
23. AttrModifier 同步崩溃异常
24. 蓝图冲突解决工具
25. 技能搜索工具
26. FDelegateBase实现，UE4反射的实现
27. NetDriver里的ChannelDefinitions是哪里注册进去的 