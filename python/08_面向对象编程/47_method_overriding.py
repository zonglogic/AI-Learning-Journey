'''
    该案例演示了方法的重写
'''

class person:
    home="earth"
    
    def __init__(self,name):
        self.name=name
    
    def eat(self):
        print("eating")

class Chinese(person):
    color="yellow"
    #重写父类方法
    def eat(self):
        print("用筷子吃")
        
y1=Chinese("zs")
y1.eat()





























