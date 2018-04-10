#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-StringIO和BytesIO：StringIO（读取字符串）
    # 使用场景：
        很多时候，数据读写不一定是文件，也可以在内存中读写。
        StringIO顾名思义就是在内存中读写str。
        要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可；
        要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取；
'''
# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
from io import StringIO
# 创建并初始化StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
# 像读文件一样，按行读取
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())    

'''
    #注：


'''