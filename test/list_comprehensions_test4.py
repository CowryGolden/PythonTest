#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 列表生成式练习：for循环可以同时使用两个或多个变量，比如dict的item()可以同时迭代key和value：
'''
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L = [k + '=' + v for k,v in d.items()]
print('L =', L)

'''
    #注：
'''