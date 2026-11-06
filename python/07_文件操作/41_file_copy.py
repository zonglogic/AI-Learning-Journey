#该案例演示文件的拷贝操作
#定义一个函数,完成文件拷贝操作

def copy_file(source_file_path,target_file_path):
    #建立连接
    source_file = open(source_file_path,"rb")
    target_file = open(target_file_path,"wb")

    #先从磁盘读取数据
    content = source_file.read()    #如果是大文件,会爆内存
    while content:= source_file.read(1024):

        #将读取的数据写入到目标文件中
        target_file.write(content)

    #关闭连接
    source_file.close()
    target_file.close()

copy_file("test.txt","D:\\Learning_Code\\python\\test_copy.txt")








