'''
 面向对象三大特性
    封装
        面向对象的封装主要指的时成员的私有化
        私有化,只能在类的内部访问成员,在类的外部成员就不能访问了
        私有化(属性和方法都可以私有化)的实现方式:
            _名    :只是一个约定,不具备强制性,想访问还是可以访问
            __名_  :在类的外部无法访问,只能在类中访问私有成员
    继承
    多态
'''

'''
    封装
'''

# 成员名 以单下划线开始,只是个标记,不具备强制性


class Girl:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def guangjie(self):
        print("gaungjie")


ls = Girl("ls", 20)
print(ls.name)
print(ls._age)

# 私有化的实现原理:底层通过改名实现私有化  _类名__名
# 成员名 以双下划线开始,至多一个下划线结束,具有强制性


class Girl1:
    def __init__(self, name, age):
        self.name = name
        self.__age_ = age

    # 在类的内部可以访问age属性
    def guangjie(self):
        print(f"{self.__age_}的{self.name}gaungjie")


lh = Girl1("lh", 20)
print(lh.name)
# print(lh.__age_)  在类的外部访问不了age属性
lh.guangjie()


class Girl2:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 在类的内部可以访问age属性
    def guangjie(self):
        print(f"{self.__age}的{self.name}gaungjie")

    # 这些装饰器的命名是固定的
    # property中有setter,getter,deleter三个对象
    # 将方法转换成属性 只读属性
    # property装饰的方法不要和变量重名,否则可能会导致无限递归
    # 一般方法命名: 私有属性去掉前面的下划线
    @property  # 属性的命名规则最好在setter中描述
    def age(self):
        if self.__age >= 18:
            return 18
        else:
            return self.__age
    # 要想进行修改的话

    @age.setter
    def age(self, age):
        self.__age = age


ch = Girl2("amy", 19)
print(ch.age)
ch.age = 16
print(ch.age)

'''
    继承
        单继承
            class 子类(父类)
        多继承
            class 子类(父类1,父类2,...)
        复用父类中的方法
            super().方法()
                super():super()不是简单的调用父类,而是基于方法解析顺序(mro) 调用当前类再mro链中的下一个类
                
            父类.方法()
'''

# 单继承


class Person:
    '''人的类'''
    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating...")


class YellowRace(Person):
    '''黄种人'''
    color = "yellow"


class WhiteRace(Person):
    '''白种人'''
    color = "white"


# 创建子类实例时把父类的__init__方法继承下来了
yr = YellowRace("zs")

print(yr.home)
print(yr.name)
print(yr.color)
yr.eat()

# 多继承


class Person1:
    '''人的类'''
    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating...")


class YellowRace1(Person1):
    '''黄种人'''
    color = "yellow"

    def eat(self):
        print("eating")

    def run(self):
        print("running")


class Student(Person1):
    '''学生'''

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def Study(self):
        print("先吃再学")
        # 复用父类方法 两种方式
        # Person1.eat(self)   self.eat()
        super().eat()  
        print("Studying")

# 这时没必要继承Person1,因为YellowRace1和Student已经继承了Person1


class ChineseStudent(YellowRace1, Student):
    country = "China"


# 获取继承链的关系
print(ChineseStudent.__mro__)
# 调用方法时先在子类中查找,若不存在则从左到右依次查找父类中是否包含方法
# 方法名相同时,先到子类中找,若没有则从左至右从父类中找
cs = ChineseStudent("zs", 80)
cs.Study()

'''
多态
    同一个事务在不同场景下的不同状态
    
'''

#在方法的参数中使用多态
class animal:
    def go(self):
        pass
    
class dog(animal):
    def go(self):
        print("跑")

class fish(animal):
    def go(self):
        print("游")

def run(ani):
    ani.go()

xh = dog()
nm = fish()

run(xh)
run(nm)

#在返回值中使用多态
def create_ani(flag):
    match flag:
        case 1:
            ani = dog()
        case 2:
            ani = fish()
        case _:
            ani=None
    return ani

print(type(create_ani(1)))

#在声明变量时使用多态
dog = create_ani(1)
fish = create_ani(2)

ani_list=[dog,fish]
for ani in ani_list:
    ani.go()
    


