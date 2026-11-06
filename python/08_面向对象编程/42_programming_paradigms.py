'''
该案例描述了面向过程(POP),面向对象(OOP),面向函数(FP)三种编程思想的区别
'''

#面向过程(POP)编程思想:把整个过程拆解成一个一个函数
def buy():
    print("去超市购买食材。")
def wash():
    print("清洗蔬菜。")
def cut():
    print("切菜。")
def cook():
    print("开始烹饪。")
def serve():
    print("上菜啦！")

buy()
wash()
cut()
cook()
serve()

#面向对象(OOP)编程思想:把整个过程拆解成一个一个对象,对象中包含属性和方法
class Dish:
    def __init__(self, name):
        self.name = name
    def prepare(self):
        pass
class Salad(Dish):
    def prepare(self):
        print(f"为 {self.name} 购买食材。")
        print(f"清洗 {self.name} 的蔬菜。")
        print(f"切 {self.name} 的蔬菜。")
class Stew(Dish):
    def prepare(self):
        print(f"为 {self.name} 购买食材。")
        print(f"切 {self.name} 的肉。")
        print(f"烹饪 {self.name}。")
class Soup(Dish):
    def prepare(self):
        print(f"为 {self.name} 购买食材。")
        print(f"煮 {self.name}。")
salad = Salad("蔬菜沙拉")
stew = Stew("炖肉")
soup = Soup("西红柿鸡蛋汤")

salad.prepare()
stew.prepare()
soup.prepare()

#面向函数(FP)编程思想:把整个过程拆解成一个一个函数,函数之间通过参数传递数据
def prepare_dish(dish_name, dish_type):
    if dish_type == "salad":
        print(f"为 {dish_name} 购买食材。")
        print(f"清洗 {dish_name} 的蔬菜。")
        print(f"切 {dish_name} 的蔬菜。")
    elif dish_type == "stew":
        print(f"为 {dish_name} 购买食材。")
        print(f"切 {dish_name} 的肉。")
        print(f"烹饪 {dish_name}。")
    elif dish_type == "soup":
        print(f"为 {dish_name} 购买食材。")
        print(f"煮 {dish_name}。")

prepare_dish("蔬菜沙拉", "salad")
prepare_dish("炖肉", "stew")
prepare_dish("西红柿鸡蛋汤", "soup")











