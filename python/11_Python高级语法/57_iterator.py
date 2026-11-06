'''
讲述迭代器
遍历
    将数据一个个取出来
循环
    遍历的一种实现方式
迭代
    遍历的一种实现方式
        for循环的底层就是迭代器,通过next函数,将一个个数据取出来

可迭代对象
    能用for循环遍历的都是可迭代对象
    -list tuple dict set str 文件
    -generator
    存在__iter__()方法
    
迭代器
    应该有两个方法:__iter__(),__next__()
        __iter__():当调用iter(对象) 底层会自动调用__iter__()这个魔法方法,获取当前对象对应的迭代器
        __next__():当调用next(对象) 底层会自动调用__next__() 这个魔法方法,获取下一个值
'''


class Reverse:

 """对一个序列执行反向循环的迭代器。"""



def __init__(self, data):

    self.data = data

    self.index = len(data)



    def __iter__(self):

        return self



    def __next__(self):

        if self.index == 0:

            raise StopIteration

        self.index = self.index - 1

        return self.data[self.index]



rev = Reverse([2, 3, 5, 7, 11, 13, 17, 19])

iter(rev)

for char in rev:

    print(char)


















