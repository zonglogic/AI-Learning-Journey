# 字符串的编码和解码

str1= "你好中国"

print(type(str1))

# 编码   默认使用utf-8编码 

b=str1.encode()

print(b,type(b))

# 解码

str2=b.decode()
print(str2,type(str2))
#编码使用的字符集要与解码一致