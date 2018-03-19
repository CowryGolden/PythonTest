#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 自定义一个函数，将参数改为可变参数
# eg:计算 a^2 + b^2 + c^2 + ...
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

list = [1,2,3]
tuple = (1,3,5,7)
print('list = [1,2,3] 各元素的平方和为:', calc(*list))
print('tuple = (1,3,5,7) 各元素的平方和为:', calc(*tuple))
print('calc(1,2,3) =', calc(1,2,3))
print('calc() =', calc())

'''
    #注：定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面增加一个 * 号。
    在函数内部，参数numbers接受一个tuple，因此函数代码完毕不变，但是调用时可以传入任意个参数，包括0个参数;
    Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去;
    *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
    eg:>>> nums = [1, 2, 3]
       >>> calc(*nums)
'''