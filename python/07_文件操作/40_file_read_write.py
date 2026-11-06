# 介绍python的文件操作方法

'''
#向磁盘文件写数据
#建立和磁盘文件的连接(通道)
file = open("test.txt","w")

#写数据
file.write("hello world\n")
file.write("hello python\n")
#关闭连接
file.close()

'''

#从文件中读取数据
#read方法
#打开文件
file = open("test.txt","rt")
'''
#read 读取文件全部内容(可以加参数)
content = file.read(8)  # 读取数据的单位取决于读取数据的方式,以文本形式读取:单位为字符.以二进制形式读取:单位为字节
content1=file.readline() #读取整行数据,读取的内容取决与此时光标的位置
print(content)
print(content1)
'''
#readlines 读取文件的所有行数据,放到列表中,若给定size>0,返回总和大约为size字节的行,实际读取的可能比size大
content = file.readlines() 
print(content)
#关闭连接
file.close()
















