#演示列表的常用函数


#extend
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)        #+创建新的对象,extend在原列表追加新元素

#remove 删除第一次出现的x
list1.remove(1)
print(list1)

#pop 删除指定位置元素,默认为末尾元素,可返回被删除的元素
print(list1.pop(2))

#clear 清空列表元素

#sorted(list[,reverse=true])降序排序
#返回排序后的新列表
#list.sorted([reverse=true]) 对列表就地排序

#反转列表元素 list.reverse()

#list.index(x[,end]) 返回x在列表中第一次出现的位置,可指定起始和结束范围

#list.count(x) 返回x的数量

#list.copy()拷贝列表

