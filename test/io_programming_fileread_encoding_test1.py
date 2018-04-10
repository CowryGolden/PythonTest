#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-文件读写：读文件(encoding的使用，要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数)
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
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
with open('E:/PythonWorkspace/test/test_gbk.txt', 'r', encoding='gbk') as f:
    print(f.read())

# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
# 因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
with open('E:/PythonWorkspace/test/test_gbk.txt', 'r', encoding='utf-8', errors='ignore') as f:
    print(f.read())

r'''
    #注：line:21如果换成 encoding='utf-8'，则报错：
    Traceback (most recent call last):
    File "e:\PythonWorkspace\test\io_programming_fileread_encoding_test1.py", line 22, in <module>
        print(f.read())
    File "D:\ProgramFiles\Python364\lib\codecs.py", line 321, in decode
        (result, consumed) = self._buffer_decode(data, self.errors, final)
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb2 in position 0: invalid start byte

'''