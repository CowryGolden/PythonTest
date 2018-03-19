#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-高阶函数-map/reduce练习：实现数字字符串转数字；（str2int，str2float）
'''
from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print("str2int('0') =", str2int('0'))
print("str2int('12300') =", str2int('12300'))
print("str2int('0012345') =", str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            #print('乘10前point =', point)
            point = point * 10
            #print('乘10后point =', point)
            return f + n / point
    return reduce(to_float, nums, 0.0)

print("str2float('0') =", str2float('0'))
print("str2float('123.456') =", str2float('123.456'))
print("str2float('123.45600') =", str2float('123.45600'))
print("str2float('0.1234') =", str2float('0.1234'))
print("str2float('.1234') =", str2float('.1234'))
print("str2float('120.0034') =", str2float('120.0034'))

'''
    #注：
'''