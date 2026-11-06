'''
该案例演示了MRO以及super混合使用
'''

class Parent1:
    def __init__(self,value1,**arg):
        print("Initializing parent1")
        self.value1=value1
        super().__init__(**arg)

class Parent2:
    def __init__(self,value2,**arg):
        print("Initializing parent2")
        self.value2=value2
        super().__init__(**arg)
        
class Child(Parent1,Parent2):
    #在子类中重复初始化
    '''
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2
    '''
    def __init__(self,value1,value2):
        print("Initializing Child")
        # Parent1.__init__(self,value1)
        # Parent2.__init__(self,value2)
        super().__init__(value1=value1,value2=value2)  #关键字传参
        # super(Parent1,self).__init__(value2)     #super(MRO上的类,实例对象),__init__()➡显式指定"从哪个类的下一个位置开始找"
        #Parent1下一个位置时Parent2
#父类已经做了两个变量的初始化,只需调用父类方法即可
c=Child(1,2)
print(c.value1)
print(c.value2)

#使用super():适用于遵循MRO顺序的场景,代码可维护性和扩展性较好,特别是在复杂的多重继承结构中
#菱形问题
class A:
    def __init__(self):
        print("进入 A.__init__")
        super().__init__()

class B(A):
    def __init__(self):
        print("进入 B.__init__")
        super().__init__()   # super(B, self)

class C(A):
    def __init__(self):
        print("进入 C.__init__")
        super().__init__()   # super(C, self)

class D(B, C):
    def __init__(self):
        print("进入 D.__init__")
        super().__init__()   # super(D, self)

D()




















