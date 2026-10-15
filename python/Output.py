# 输出


# print中有个end参数,默认是"\n",以什么为结尾

print("hello",end=" ")

print("world")

# 格式化输出 
# 字符串中用%占位

# 整数:%d  小数:%f  字符串:%s  %.2f表示保留两位小数

int1=10
float1=2.3

print("int1=%d,float1=%f" %(int1,float1))

#f字符串格式化
bool1=True


print(f"int1={int1},float={float1},bool1={bool1}")


#数字格式化

float2=31415.9
str2="{:*^20,.2f}".format(float2)  # 居中对齐
print(str2)
str2="{:*>20,.2f}".format(float2)  # 右对齐
print(str2)
str2="{:*<20,.2f}".format(float2)  # 左对齐
print(str2)


#可以用{}来转义大括号

