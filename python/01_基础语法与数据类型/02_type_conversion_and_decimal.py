# 使用Decimal解决浮点数精度丢失问题
"""
from decimal import Decimal
num1=Decimal("0.1")
num2=Decimal("0.2")
print(num1+num2)  #解决精度丢失问题
num3=0.1
num4=0.2
print(num3+num4)
"""


# 强制类型转换
#int(x,base)  转换成int类型,base表进制数
#float(x)    转换浮点数类型
#complex(x,y)  创建一个实部为x,虚部为y的复数
#str(x)  转换成字符串类型
#repr(x)    转换成字符串,可以转义字符串中的特殊字符
#eval(x)    将字符串x当成有效的表达式来求值并返回计算结果
#bin()
#hex()
#ord()    转换ASCII码
#chr()    转换成Unicode字符