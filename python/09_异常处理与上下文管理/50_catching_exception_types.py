'''
演示了处理不同类型的异常

当程序运行过程中,如果发生异常,底层原理
    如果程序执行的过程中,发生了异常,底层会创建一个对应异常类型,然后将这个异常抛出(raise)
    当调用者接收到异常对应之后,可以通过except代码对异常对象进行捕获,在except代码块中对异常进行处理,如果没有被except捕获,那么异常会继续向上抛出
    直到交给计时器,解释器默认处理方式是将那个异常信息打印到控制台,程序终止

except可以针对不同类型异常进行处理
    try:
        可能发生异常的代码块
    except 异常类型1 as 别名:
        处理方式1
    except 异常类型2 as 别名:
        处理方式2
    except (异常类型3,异常类型4,异常类型5) as 别名:
        处理方式3
    except Exception as e:
        处理方式4
'''
try:
    num1 = int(input("请输入第一个数字："))
    num2 = int(input("请输入第二个数字："))
    res = num1 / num2
    print(f"结果：{res}")
except ValueError:
    # 处理：不能转成数字（输入字母、符号）
    print("异常：输入不是有效的整数！")
except ZeroDivisionError:
    # 处理：除数为0
    print("异常：除数不能为0！")
except Exception as e:
    # 兜底：捕获上面没覆盖到的其他所有异常
    print(f"其他未知异常：{e}")
else:
    # 没有发生任何异常才会执行
    print("计算顺利完成，没有报错")
finally:
    # 无论有没有异常，一定会执行
    print("=== 程序本次计算结束 ===")
#一般将资源释放的代码放在finally语句中
#如果异常没有被捕获,捕获过程中发生新的异常,或者有return时,仍然执行finally语句




















