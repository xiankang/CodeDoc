# prefab


## 什么是prefab

场景内的游戏对象及其组件、属性等序列化后就成了prefab，用于资源及配置的复用。加载到场景后，又成了游戏对象，即prefab的实例化。



## prefab与prefab varient

prefab varient是基于prefab的变体，可以复写基prefab的属性，但是不能增加和删除组件，不能调整层级


## prefab有哪些操作


## prefab实例与prefab asset
prefab实例是指在场景中通过prefab实例化后的游戏对象，或者场景中的游戏对象拖到项目中序列化就成了prefab asset（在硬盘上了）

## revert与apply

revert是指回滚prefab实例中的复写

apply是指把prefab实例中的复写应用到prefab asset