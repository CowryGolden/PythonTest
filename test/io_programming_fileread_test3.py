#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-文件读写：读文件(控制IO错误：with 语句的实现)
    # 使用场景：
        读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
        读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
        现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
        然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
        
        读文件
        要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：

'''
# 由于每次使用try ... finally来实现实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with open('E:/PythonWorkspace/test/test.txt', 'r') as f:
# with open('E:/PythonWorkspace/test/test1.txt', 'r') as f:
    print(f.read()) 

# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

'''
    #注：


'''