#list 可变有序

#可以通过[元素1,元素2,元素3]或者list()创建空列表

list1 = [100,200,300,400,500]

#有两套下标,起始从0开始,末尾-1开始

#通过索引获取列表中的元素
print(list1[2])
print(list1[-3])

#列表的切片
'''
print(list1)
print(list1[:])
print(list1[2:4]) #左开右闭
print(list1[2:-1])
'''
#向列表中添加元素
#append像列表末尾追加元素
list1.append(600)

#insert 像列表中指定位置插入元素
list1.insert(2,0)   #在下标2处插入0
print(list1)

#列表的相加
list2=["a","b","c"]
print(list1 + list2)

#列表的乘法
print(list1 * 2)  #不是元素×2,而是输出两份list1

#修改列表中的元素
list1[2]=700
print(list1)

#通过切片修改列表中的元素
list1[2:5]=['a','b','c']
print(list1)

#检查成员是否为列表中的元素
print(30 in list1)

#获取列表长度
print(len(list1))

#对列表中的元素求和,求最大值,最小值
list2=[10,20,30]
print(sum(list2))
print(max(list2))
print(min(list2))

#列表的遍历,将列表中的元素一个一个取出来
for item in list1:
    print(item)

#通过下标获取列表中的元素
for i in range(len(list1)):
    print(list1[i])

#同时获取列表的下标以及对应的值
for i,v in enumerate(list1):
    print(i,v)              #同时获取下标和值

#从列表中删除元素
del list1[2]
print(list1)

#列表的嵌套
list2 = [10,20,30,['a','b','c']]
print(list2[3][1])    #取第四个元素的第二个值

#列表推导式
list3 = [i**2 for i in range(0,5)]
print(list3)

#带条件的列表推导式
list3 = [i**2 for i in range(10) if i%2==0]
print(list3)

#使用现有列表创建新的列表
list4 = [i*2 for i in list3]
print(list4)

#包含多个循环的列表推导式
list5 = [f"{i}-->{j}" for i in list3 for j in list4]
print(list5)

#zip函数 将多个可迭代对象打包为一个个元组
zipped = zip(list3,list4)
print(list(zipped))




