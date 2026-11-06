'''
该案例演示了raise
'''

#两个整数的加法运算

def add(num1,num2):
    if isinstance(num1,int) and isinstance(num2,int):
        return num1+num2
    else:
        #抛出异常 #单独会终止程序,需要与异常处理代码块配合
        raise TypeError("参数类型错误")
   
try:
    res=add(1.0,2)
except TypeError as e:
    print(e)
else:
    print(res)

#assert
def int_add(x,y):
    assert isinstance(x,int) and isinstance(y,int),"参数类型错误"
    return x+y

int_add(10,20)

#自定义异常类型
class MyException(Exception):
    pass

def get_age(age):
    if age>=200 or age<=0:
        raise MyException("年龄不合法")
    else:
        print(age)

get_age(-1)




















