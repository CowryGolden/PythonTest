#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 列表生成式练习：列出当前目录下的所有文件和目录名。
'''
import os # 导入os模块
L = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print('L =', L)

'''
    #注：
'''