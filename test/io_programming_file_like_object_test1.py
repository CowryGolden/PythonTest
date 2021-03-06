#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-文件读写：读文件，file-like Object
    # 使用场景：
        读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
        读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
        现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
        然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
        
        读文件
        要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：

'''
# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。



'''
    #注：


'''