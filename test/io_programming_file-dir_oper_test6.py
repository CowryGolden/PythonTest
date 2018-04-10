#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-操作文件和目录：练习-实现win下的dir或Linux下的ls -lrt列出当前目录相关信息
    # 使用场景：
        编写一个程序，实现win下的dir或Linux下的ls -lrt列出当前目录相关信息
'''
# 编写一个程序，实现win下的dir或Linux下的ls -lrt列出当前目录相关信息
import os
import time

class MyLs(object):
    def __init__(self, dir='.'):
        self.dirList = os.listdir(dir)

    def ls(self):
        fileLists = []
        for file in self.dirList:
            print(self.getFileInfo(file))

    def getFileInfo(self, fileName):
        size = str(os.path.getsize(fileName))
        fileType = 'd' if os.path.isdir(fileName) else '-'
        readAble = 'r' if os.access(fileName, os.R_OK) else '-'
        writeAble = 'w' if os.access(fileName, os.W_OK) else '-'
        operAble = 'x' if os.access(fileName, os.X_OK) else '-'
        timestamp = os.path.getctime(fileName)
        timeLocal = time.localtime(timestamp)
        dt = time.strftime('%Y-%m-%d', timeLocal)

        return fileType + readAble + writeAble + '\t' + operAble + '\t' + size + '\t' + dt + '\t' + fileName

if __name__ == '__main__':
    myls = MyLs()
    myls.ls()

r'''
    #注：   
待优化代码：

import os
from os import walk

def get_item(path, item):
    f = []
    for(dirpath, dirnames, filenames) in walk(path): # 遍历所有文件及文件夹
        f.extend([
            (os.path.join(dirpath, m)).lstrip(path) for m in filenames if item in m  # 遍历所有文件，截取相对目录，并将满足条件的n放到f中
        ])
        f.extend([
            (os.path.join(dirpath, m)).lstrip(path) for m in dirnames if item in m  # 遍历所有目录，截取相对目录，并将满足条件的n放到f中
        ])
    return f

a = get_item(os.path.abspath('.'), 'test')
for i in a:
    print(i)    

'''