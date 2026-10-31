# 演示了递归的案例 求阶乘


#循环
def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

print(factorial(5))

#递归
def factorial_1(n):
    if n==1:
        return 1
    return n * factorial(n-1)
    
print(factorial(5))




























