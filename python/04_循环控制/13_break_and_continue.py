#循环关键字
#0-9,跳过偶数
'''
for i in range(10):
    if i%2==0:
        continue
    print(i)

'''
sum =0
for i in range(10):
    sum=sum + i**i     #**表示幂
    if sum>1000000:
        break
    print(i,sum)

#pass 是空语句,保持程序结构的完整性,用于占位语句





