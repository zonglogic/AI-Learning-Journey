#字符串 不可变 有序 有下标

#创建字符串
str1="hello world"
str2="dlrow olleh"
#访问字符串  与列表相似
print(str1[-1])
print(str1[1:4])

#字符串相加
print(str1 + str2)

#检查成员是否为字符串中元素
print("lo" in str1)

print("hello\nworld")
print(r"hello\nworld")  #无转移字符
#所有字符串按照字面意思处理,没有转义字符.需在字符串前加r

