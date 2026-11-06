#该案例演示了匿名函数
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b

'''
计算机函数   可以实现对两个整数的加减乘除运算
a:整数1
b:整数2
op:运算操作(加减乘除)
'''
def calculate(a,b,op):
    return op(a,b)

print(calculate(1,2,add))

#lambda 表达式

def calculate(a,b,op):
    return op(a,b)
    
calculate(10,20,lambda x,y: x + y)

#匿名函数的使用
#提供一个万能的函数,可以对列表中每一个元素进行处理,处理的逻辑交给调用者



def my_map(func,list11):
    new_list=[]
    for item in list11:
        new_list.append(func(item))
    return new_list

list1=[1,2,3]

print(my_map(lambda item:item*2 ,list1))


def ff(dic1):
    return dic1["age"]

student_list = [{"name": "zhang3", "age": 36}, {"name": "li4", "age": 14}, {"name": "wang5", "age": 27}]
print(sorted(student_list, key=ff))


#map()
#map()函数对序列中元素逐一处理: map(func,list)
print(list(map(lambda x :x*2 ,list1)))
#filter()
#对序列中的元素过滤
print(list(filter(lambda x:x>1 ,list1)))
#reduce()
#对序列中的元素进行累积













