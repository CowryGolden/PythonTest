#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-操作文件和目录：练习-查找当前目录以及当前目录的所有子目录下包含指定字符串的文件
    # 使用场景：
        编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
'''
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os

def searchFile(findstr, currpath, fpath):
    for x in currpath:
        if os.path.isdir(x):
            searchFile(findstr, os.listdir(x), os.path.join(fpath, x))
        elif findstr in x:
            print(os.path.join(fpath, os.path.split(x)[1]))
    return        

if __name__ == '__main__':
    searchFile('bug', os.listdir('.'), os.path.abspath('.'))

r'''
    #注：   

'''