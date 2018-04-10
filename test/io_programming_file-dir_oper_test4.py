#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-操作文件和目录：os和os.path模块操作文件和目录；过滤文件
    # 使用场景：
        操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。
        最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录；过来某一个后缀名的文件；
'''
# 过滤文件
import os
# 列出当前目录下的所有目录
dirlist = [x for x in os.listdir('.') if os.path.isdir(x)]
print('dirlist =', dirlist)

# 要列出所有的.py文件
pyfile = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print('pyfile =', pyfile)


r'''
    #注：把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
            part-1/part-2
        而Windows下会返回这样的字符串：
            part-1\part-2
        同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
            >>> os.path.split('/Users/michael/testdir/file.txt')
            ('/Users/michael/testdir', 'file.txt')
        os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
            >>> os.path.splitext('/path/to/file.txt')
            ('/path/to/file', '.txt')
        这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。    

'''