"""
 该案例讲述面向对象
 面向对象
    对象
        在自然界中,只要客观存在的事物,都是对象
    类
        对大量对象具有相同属性和行为的抽象描述,称为类
            有什么
                属性
            能做什么
                方法
        类是创建对象的模板
        类是客观事物在人脑中的主观反应
    
    类定义的语法
        class 类名:
            '''类说明文档'''
            属性
                类属性|类变量
                实例属性|实例变量
            方法
                类方法
                静态方法
                实例方法
"""
# 类的定义


class persons:
    """人的类"""
    # 类属性--会被当前类的所有实例(对象)共享
    home = "earth"
    # self 代表被创建出来的对象

    def __init__(self, name, age):
        # 实例属性--每一个实例独有
        self.name = name
        self.age = age
    # 实例方法

    def eat(self, food):
        print(f"{self.name}正在吃{food}")

    def drink(self, drink):
        print(f"{self.name}正在喝{drink}")


# 类的操作
# 成员引用:获取类的成员
print(persons.__doc__)  # 类说明文档
print(persons.home)  # 类属性
print(persons.eat)
print(persons.__init__)

# 实例化


class student:
    # 类属性
    school = "atguigu"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.age}岁的{self.name}正在{self.school}学习")


# 创建对象 ---底层调用__init__方法
mn = student("mn", 18)
print(type(mn))
print(mn.name)
print(mn.age)
print(mn.school)
mn.study()

'''
对象的创建过程
    当执行对象的创建操作的时候
    底层首先调用__new__()的方法,__new__的作用是创建当前类的实例出来
    然后在__new__()方法中调用__init()方法,并在调用的时候,会将创建出来的实例作为__init__()的第一个参数传递过去
    在__init__()方法中,主要给创建出来的对象添加实例属性以及属性赋值
    def __new__():
        new_obj = 创建对象
'''


class person:
    def eat(self):
        print("eating")


p = person()
p.eat()
person.eat(p)
# 注意__init__()方法不是必须的,如果没有定义类的时候显示提供__init__(),默认会提供一个只有一个参数self的init方法
# 但是self这个参数,不需要我们传递,self是一个约定俗成的名字,代表当前创建的对象

jh = student("jh", "18")

jh.study()

# 类属性
# 添加类属性  类名.属性名=值
student.aaa = "test"
student.bbb = "test"

# 实例.属性名=值
jh.school = 1

#方法
class Person1:
    home="earth"
    #类方法  可以在不创建实例的情况下调用,通过类名直接调用,可以被类和实例调用
    @classmethod   #装饰器
    def class_method(cls):
        print("class_method",cls.home,cls.__doc__)
    #实例方法
    def run(self):
        print("1")
    #静态方法  不访问类属性和实例属性,只依赖与传入的参数,适用于工具函数,不需要类和实例的信息
    @staticmethod
    def m1():
        print("static_method")
        
Person1.class_method()

#实例方法不创建实例会报错
# Person1.run()

#魔法方法  __method__ 不需要我们手动调用,当执行某个特定操作时,这类方法会自动调用

#__new__,__init__,__del__,__

class person2:
    pass

p2=person2()
del p2    #删除p2对象  当引用计数变为0时才会执行__del__魔法方法













