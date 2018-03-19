#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-高阶函数-map/reduce练习：使用map/reduce函数实现：将字符串类型数字转为int类型数字功能(使用lambda函数)
'''
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def char2num(s):
        return DIGITS[s]
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print("str2int('13579') =", str2int('13579'))

'''
    #注：reduce必须接收两个参数，reduce把结果继续和序列的下一个元素做累计计算，其结果就是：
        reduce(f, [x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
'''