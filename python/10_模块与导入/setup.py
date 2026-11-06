from distutils.core import setup
'''
setup 打包操作
在文件外部建立setup.py文件
在当前文件目录下的命令行中输入 python setup.py build . python setup.py sdist
安装本机已有的包的压缩包    pip install 压缩包的文件路径

'''



setup(

    name="graphic", # 需要打包的名字

    version="1.0", # 版本

    py_modules=["graphic.circle", "graphic.rectangle"], # 需要打包的模块

)
