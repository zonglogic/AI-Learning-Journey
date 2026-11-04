'''
描述with语句

    with expression或者对象 as variable:
        #代码块
    说明:
        expression:是一个对象或者是函数调用,要求返回的内容类型必须是上下文管理器对象类型
            上下文管理器类中的有两个方法必须提供:__enter__和__exit__方法
            
        variable:是可选的,用于存储expression的__enter__方法的返回值
    
    执行原理:
    当执行with语句是,会调用expression对象的__enter__方法
    __enter__方法的返回值可以被储存在variable中(如果有),以供with代码块中使用
    __enter__方法的返回值一般是self(当前上下文管理器对象)
    执行with代码块中内容
    当代码块执行完毕之后,不管是否发生异常,都会执行上下文管理器对象的__exit__方法,在__exit__方法中.将资源释放掉

'''
'''
try:
    try:
        file=open("test.txt","w")
        file.write(a)
        file.close()
    except:
        print("异常")
    finally:
        file.close()
finally:
    print(file.closed)
'''
#with自动释放资源
print(type(open("test.txt","w")))
try:
    with open("test.txt","w") as file:
        file.write()
finally:
    print(file.closed)
    



























