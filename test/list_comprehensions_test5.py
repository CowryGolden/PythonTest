#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 列表生成式练习：使用內建的isinstance函数判断一个变量是否为字符串，将L1中所有的字符串转换后小写，并生成结果列表
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L = [s.lower() for s in L1 if isinstance(s, str)]
print('L =', L)

'''
    #注：
'''