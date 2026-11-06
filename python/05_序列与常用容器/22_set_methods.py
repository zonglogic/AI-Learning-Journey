set1={1,2,3,4,5,6,7,8}

#set.update(x)   添加元素,x可为列表元组字符串字典等可迭代对象

#set.union(x)    添加元素后返回一个新的集合,x可为列表元组字符串字典

#set.discard(x)   移除元素,不会报错

#set.pop()    随机删除集合里的元素

#set.clear()

#set.difference(x1)     求set与x1的差集 set有但x1没有

#set.difference_update(x1)     返回一个新的集合,对set修改

#set.intersection(x1)     求set与x1的交集
#set.intersection_update(x1)    返回新的集合   

#运算符
'''
set1 & set2   求集合交集
set1 | set2   求集合并集
set1 - set2   求集合差集

'''

#set1.isdisjoint(set2)   判断两集合是否没有交集

#set1.issubset(set2)    判断set1是否为set2的子集

#set1.issuperset(set2)   判断set2是否为set1的子集

#set1.symmetric_difference(set2)   求两集合中不重复的元素,返回一个新的集合

#set1.symmetric_difference_update   求两集合中不重复的元素

#set.copy()   拷贝集合

