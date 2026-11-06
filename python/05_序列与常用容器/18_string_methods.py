# 字符串中常用函数

str1="hello"
str2="world"
str3="name,age,gender"
#str.replace(old,new,max) 把字符串的old元素替换成new ,替换次数不超过max次
print(str1.replace('l','h',1))   #字符串不可变
print(str1)

#str.split([x],[n])  按x分隔字符串,默认按任何空白字符串分隔并在结果中丢弃字符串,可指定最大分隔次数
list1=str3.split(",")
print(list1,type(list1))

#str.rsplit([x],[n]) 与split类似,从右边开始分隔


#x.join(seq)  以x作为分隔符,将序列中所用字符串合并为一个新的字符串
list2=['10','20','30']    #只能是字符串形式的序列
print(','.join(list2))

#str.strip([x])  截掉字符串两边的空格或指定字符
str4="   hello   "
print(str4.strip(" "))

#str.lstrip()截掉左   str.rstrip()截掉右

#str.removeprefix()  截掉字符串指定前缀
print(str4.removeprefix("   "))  #指定什么去掉什么

#str.removesuffix()   截掉字符串指定后缀

#str.upper()   将所有字符串转为大写

#str.lower()   将所有字符串转为小写

#str.swapcase()   将字符串的字母大小写反转

#str.capitalize()   将字符串的第一个字母变为大写,其他字母变小写

#str.title()        将字符串的每个单词首字母都大写

#str.casefold()     返回适合无大小写比较的字符串版本,加强版的lower()

#len(str)      返回字符后长度

#min() max()返回最大最小值

#str.find(x,start,end)  返回字符串中的第一个x的索引值,不存在则返回-1,可指定字符串的开始结束范围

#str.rfind(x,start,end) 从右开始查找

#str.index(x,start,end) 返回字符串中第一个x的索引值,不存在则报错,可指定范围

#str.rindex(x,start,end) 从右开始索引

#str.count(x,start,end)  返回x在字符串中的个数,可指定范围

#str.startwith(x) str,endwith(x)  检查字符串是否以x开头/结尾

#str.isspace()检查字符串是否非空且包含空白

#str.isalnum() 检查字符串是否非空且只包含字母(英文字母+汉字)和数字

#str.isalpha()  检查字符串是否非空且只包含字母(英文字母+汉字)

#str.isascii    检查字符串是否只包含ascii字符,空字符串也是ascii

#str.isdecimal()  检查字符串是否非空且只包含十进制字符(仅匹配十进制数字字符)

#str.isdigit()   检查字符串是否非空且只包含数字(包含isdecimal()的范围+上下角标数字)

#str.isidentifier()   检查字符串是否是有效标识符

#str.isnumeric()      检查字符串是否非空且只包含数值字符(包含isdigit()范围+中文数字,罗马数字,分数)
