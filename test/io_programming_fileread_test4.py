#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-文件读写：读文件(readline()和readlines()的使用)
    # 使用场景：
        读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
        读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
        现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
        然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
        
        读文件
        要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符；
        eg:    f = open('E:/PythonWorkspace/test/test.txt', 'r')
        
        调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，
        可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，
        调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

'''
# 调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
with open('E:/PythonWorkspace/test/test_1.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())  # 去除前后空格，并把末尾的'\n'删掉

'''
    #注：


'''