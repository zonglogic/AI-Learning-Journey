# 分支的嵌套

#定义一个变量表示状态码
state=0b010

#取二进制数的各个位置的取值 在对应位置 & 1
if state & 0b100 == 0b100:        #取第一个位置的值
      #大写
      print("大写")
else:
     print("小写")
     if state & 0b010 == 0b010:
            if state & 0b001 == 0b001:
                print("中文")
            else:
                print("英文")
     else:
          print("美式键盘")



