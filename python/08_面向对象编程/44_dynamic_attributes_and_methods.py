'''
 该案例描述动态添加属性
'''

import types

class person:
    def __init__(self, name):
        self.name = name
    def m1(self):
        self.address="北京"
        
        
#不在类中   
def eat():
    print("eating")
    
def drink(self):
    print("Drinking")

@classmethod
def come_from(cls):
    print("earth")

@staticmethod
def static_function():
    print("static_function")

p = person('ZS')
print(p.name)
p.age = 20
print(p.age)
p.m1()       #使用之前要先调用方法
print(p.address)
#给类添加属性
person.home="earth"

#动态的给实例添加方法
zs=person("zs")
zs.aa="xxx"
zs.bb=eat
zs.bb()
#给实例添加实例方法 
zs.aa = types.MethodType(drink,zs)

zs.aa()

#动态的给类添加类方法
person.come_from=come_from

#动态的给类添加静态方法
person.static_function=static_function

#给类的所有实例添加实例方法
def F1(self,x,y):
    print(x&y)
    
class C:
    f=F1

#动态删除
zh=person("zh")
print(zs.name)
del zh.name

#限制添加实例属性和实例方法
class person1:
    #限制实例成员只能有这三个属性
    __slots__ = ("name","age","eat")
    def __init__(self, name):
        self.name = name
    def m2(self):
        self.address="北京"

def eat(self):
    print("eating")
    
def drink(self):
    print(f"{self.name}drink")

p=person1("zs")

'''
#限制添加实例属性
p.weight=100
#限制添加实例方法
p.drink=types.MethodType(drink,p)
'''

#类中成员加载顺序
class person2:
    aa="hello"
    def __init__(self):
        self.aa="world"
    
    def aa(self):
        print("welcome")

p = person2()
print(p.aa)     #要先到实例对象里找有没有aa这个属性

person.aa       #按照后来者覆盖的方式定义类属性












