'''
描述异常的传递
    try嵌套或者函数的嵌套定义,一层一层向外传递
    如果存在函数的嵌套调用,沿着函数调用的方向反向传递
'''

try:
    try:
        try:
            print(3/0)   # 这里抛出 ZeroDivisionError
        except NameError:
            print("第1层")
    except ValueError:
        print("第2层")
except ZeroDivisionError:
    print("第3层")




def m3():
    print(3/0)


def m2():
    m3()

def m1():
    m2()

m1()


