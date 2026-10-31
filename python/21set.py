#集合
#可变,无序类型 可以向set中添加\删除元素
#set元素中不可重复,元素没有下标,不能通过下标找元素,也不能切片

set1={1,2,3,4,5}
set2=set([6,7,8,9,0])
set3=set() #创建空set

#修改set
#添加元素
set1.add(5)

#删除元素
set1.remove(5)

#检查成员是否为集合里的元素 x in set

#常规函数用法一样

#遍历集合
for i in set1:
    print(i)




