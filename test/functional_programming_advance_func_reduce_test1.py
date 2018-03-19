#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-高阶函数-map/reduce练习：使用reduce(func,Iterable)函数实现序列求和
'''
from functools import reduce

def add(x, y):
    return x + y

r = reduce(add, [1,3,5,7,9])
print('reduce(add, [1,3,5,7,9]) =', r)
print('sum([1,3,5,7,9]) =', sum([1,3,5,7,9]))

def fn(x, y):
    return x * 10 + y

r1 = reduce(fn, [1,3,5,7,9])
print('reduce(fn, [1,3,5,7,9]) =', r1)

#根据字符串数字取对应数字
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

r2 = reduce(fn, map(char2num, '13579'))
print("reduce(fn, map(char3num, '13579')) =", r2)


'''
    #注：reduce必须接收两个参数，reduce把结果继续和序列的下一个元素做累计计算，其结果就是：
        reduce(f, [x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
'''