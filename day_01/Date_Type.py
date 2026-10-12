# 使用Decimal解决浮点数精度丢失问题

from decimal import Decimal
num1=Decimal("0.1")
num2=Decimal("0.2")
print(num1+num2)
num3=0.1
num4=0.2
print(num3+num4)