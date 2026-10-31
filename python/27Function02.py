'''
该案例演示了防止函数对list表数据进行修改
'''
#函数中修改列表 --- 对外部定义的列表也有影响

#防止函数修改列表
import copy


def change_list(list1):
    list1[3].append(100)

list2=[1,2,3,[1,2,3]]
#创建一个新的对象:浅拷贝(防止不了队列内嵌套队列)
list3=list2[:]
change_list(list3)
print(list2)
#深拷贝
list4=copy.deepcopy(list2)
change_list(list4)
print(list2)



















