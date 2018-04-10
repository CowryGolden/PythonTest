#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-文件读写：读文件
    # 使用场景：
        读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
        读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
        现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
        然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
        
        读文件
        要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：

'''
# Python内置的函数open()  （标示符'r'表示读，这样，我们就成功地打开了一个文件。）
f = open('E:/PythonWorkspace/test/test.txt', 'r')
'''
# 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：
>>> f1 = open('E:/PythonWorkspace/test/test.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'E:/PythonWorkspace/test/test.txt'
'''
# 如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
s = f.read()
print(s)
# 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
f.close()



'''
    #注：


'''