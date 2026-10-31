'''
演示函数的定义

def 参数名(参数列表):
    函数体-函数实现的功能
    [return]

说明
    def是定义函数的关键字
    函数名是我们给当前完成某个功能的代码块自己取的名字--需要遵循标识符的的命名规则
    (参数列表) 函数执行的时候,需要调用者给我传递的数据
    函数完成的功能需要放到函数体中 -- 缩进
    如果函数执行完毕之后,需要给调用者返回数据,通过return进行返回

    注意函数需要先声明再调用
'''
#函数的定义
'''
#没有封装函数
#向控制台打印2*3的*
rows=2
while rows>0:
    print('*' * 3)
    rows-=1
print("~~~~~~~~~~~~~~~~~")
#封装函数
#定义函数
def print_star():
    rows=2
    while rows>0:
        print('*' * 3)
        rows-=1
#调用函数
print_star()

#带参数
def print_star_1(rows,cols):
    while rows>0 :
        print('*' * cols)
        rows-=1
#调用函数
print_star_1(2,3)
print("~~~~~~~~~~~~~~~~~")
print_star_1(3,4)

'''

#不同类型的参数
#不可变类型对象
def change_int(num):
    print(f"在函数修改数据前num的值{num},地址是{id(num)}")
    num=20
    print(f"在函数修改数据后{num}的值,地址是{id(num)}")

a=10
print(f"在函数体外调用函数前a的值{a},地址是{id(a)}")
change_int(a)
print(f"在函数体外调用函数后a的值{a},地址是{id(a)}")

#可变类型对象
def change_int(num):
    print(f"在函数修改数据前num的值{num},地址是{id(num)}")
    num.append(20)
    print(f"在函数修改数据后{num}的值,地址是{id(num)}")

list1 = [1,2,3]
print(f"在函数体外调用函数前a的值{list1},地址是{id(list1)}")
change_int(list1)
print(f"在函数体外调用函数后a的值{list1},地址是{id(list1)}")










