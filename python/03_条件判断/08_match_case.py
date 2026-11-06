# 演示match case

from random import randint

month = randint(1,12)
print(f"当前月份:{month}")

match month:
    case 1  | 3 | 5 | 7 | 8 | 10 | 12 :
        print("当前月份有31天")
    case 2 :
        print("当前月份有28或29天")
    case 4 | 6 | 9 | 11 :
        print("当前月份有30天")
    case _ :
        print("没匹配上") 

# 一般等值比较用match_case,而范围之中用if else
