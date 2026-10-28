# 演示循环的嵌套
#打印99乘法表


#外层循环控制行,内层循环控制列
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} ={i*j}", end="\t")
    print()




