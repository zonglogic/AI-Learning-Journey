# 表示for循环
'''
for 变量 in 可迭代对象:
    循环体
else:
    循环正常结束执行的代码


说明
    for是关键字
    变量用于接收当前这次遍历出来的数据
    in是关键字
    可迭代对象---列表,元组,集合,字符串
'''

# 遍历列表

list1=[10,20,30,40,50]

for i in list1:
    print(i)

#遍历字符串

str1="hello world"
for i in str1:
    print(i)

# 遍历range数列
for i in range(10):
    print(i)

#range数列
#range(start,stop,step),范围左闭右开
#生成数列,返回可迭代的对象
#start默认为0,stop不可以省略
#step是正数,表示递增数列.step是负数,表示递减数列,stop<start







