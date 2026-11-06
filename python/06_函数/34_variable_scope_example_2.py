#该案例演示了变量的作用域

#内建作用域(python自带的)

a=int('10')     #全局作用域

def outer():
    a=20        #嵌套作用域
    def inner():
        a=30    #局部作用域
        print(a)
    return inner

outer()()

'''
在程序中访问变量的时候,按照如下的顺序到不同的作用域查找
局部
嵌套
全局
内建
'''
#局部变量和全局变量
'''
python中,程序变量并不是在哪个位置都可以访问的,访问权限决定于这个变量是在哪里赋值的
局部变量
    在局部作用域中定义的


    只能在函数内部被访问

全局变量
    在全局作用域中定义的变量

    全局变量,在整个模块中都可以访问到

'''

'''
global
    在局部作用域中,声明使用的是全局变量
nonlocal
    在局部作用域中,声明使用的是嵌套变量

'''
num=10
def func():
    #num=num+10
    #当在函数内部对一个变量进行赋值操作的时候,python默认会把这个变量当作局部变量,即便全局作用域已存在同名变量
    global num
    #声明要操作的变量是全局变量
    num=20
    print(num)
    
func()
print(num)


def outer():
    num=10
    def inner():
        nonlocal num
        #声明要操作的是外部函数里的num
        num=20
        print(num)
    inner()
    print(num)

outer()




















