'''
该案例描述模块

模块的导入
    全局导入
        导入模块的所有成员
        语法
            import 模块名 as 别名
    局部导入
        语法
            from 模块名 import 成员1 as 别名,成员2 as 别名...
            
            from 模块名 import*
            带入模块中所用不以单下划线开头的成员
        使用方式
            直接通过成员名或别名进行访问
        
        在被导入的模块中,通过__all__变量设置那些成员可以被导入 注意:仅在from...import* 可以用
    
'''

#全局导入
import myadd as md
#用模块名.成员名进行访问
print(md.my_add(10,20)),

#局部导入
#方式1 导入模块指定成员
from mymulti import multi
#直接通过成员名访问
multi(10,20)

#方式2 导入所有不以单下划线开头的成员
from mymulti import*
print(num)
#print(_str1) 不可访问

#模块的查找顺序: 当前目录->pythonpath环境变量中的目录->包含标准python模块以及这些模块所依赖的任何extension module的目录
import sys 
print(sys.path)
#sys.path.append("要添加的模块的路径"),临时添加查找路径

#__all__:在被导入的模块中,通过__all__变量设置那些成员可以被导入 注意:仅在from...import* 可以用

#__name__:当一个Python文件被直接运行时,该文件的name属性值为"main".当一个Python文件作为模块被导入时,name属性会被设置为该模块的名称(即文件名，不包含.py后缀)
#         常用在测试模块文件中函数功能时

#dir() :不带参数:返回当前局部作用域的所有变量,名字列表 带参数:返回这个对象(模块/类/变量)拥有的所有属性,方法名称,按字母排序
import math
from math import pi
print(dir(pi))

#带包导入
'''
全据导入
    导入包中模块中所有成员
        import 包名.模块名 as 别名
    使用方式
        包名.模块名.成员名  别名.成员名

局部导入
方式1:
    从包中导入模块
    语法:
    from 包名 import 模块名 as 别名
方式2:
    从包中模块导入功能
    语法:
        from 包名.模块 import 成员1 as 别名
    使用方式:
        成员名/别名直接访问
    导入模块内所有成员
        from 包名.模块名 import*
    导入包下的模块
        from 包名 import*  必须在__init__.py中指定
'''

#全局导入
import graphic.circle as c
print(c.PI)

#导入包下所有模块 如果最后一项是包,必须在被导入包的__init__.py文件中,指定导入包中的哪些模块
import graphic
print(graphic.circle.PI)

#局部导入 
from graphic import circle
print(circle.PI)

#导入包中模块某个成员
from graphic.circle import area

print(area(10))






