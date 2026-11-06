# 元组
#元组是不可变的有序的元素集合,使用()定义,数据之间用,分隔
#使用方式与列表类似

tuple1=(100,200,300,400)
#也可以通过元组推导式创建元组,类似于列表
tuple_generator=(x for x in range(10))  #获取生成器对象
print(tuple_generator)
tuple2=tuple(tuple_generator)
print(tuple2)

#访问元组
print(tuple1[1])
print(tuple1[1:3])

#元组可像列表一样进行,相加,乘法运算代码相同

#检查成员是否为元组元素
print(300 in tuple1)

#获取元组长度 
print(len(tuple1))

#min() max() sum() 同样适用

#遍历元组
for i in tuple1:
    print(i)

for i in range(len(tuple1)):
    print(i,tuple1[i])

for i,v in enumerate(tuple1):
    print(i,v)

#元组所指定内存中的内容不可变,但是可以重新赋值
print(id(tuple1), tuple1) 
tuple1 = tuple1 + (1, 2, 3)  #重新创建新元组赋值
print(id(tuple1), tuple1)

#如果元组中元素是可变数据类型,其嵌套项可以被修改
tuple1 = (100, 200, 300, [1, 2, 3])   #其中的列表元素可修改
tuple1[3].append(4)
print(tuple1)  # (100, 200, 300, [1, 2, 3, 4])



