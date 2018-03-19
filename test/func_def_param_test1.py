#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 自定义一个函数，将参数作为list或tuple传入
# eg:计算 a^2 + b^2 + c^2 + ...
def calc(numbers = None):
    sum = 0
    if numbers is not None:
        for n in numbers:
            sum = sum + n * n
    return sum

list = [1,2,3]
tuple = (1,3,5,7)
print('list = [1,2,3] 各元素的平方和为:', calc(list))
print('tuple = (1,3,5,7) 各元素的平方和为:', calc(tuple))
list = []
tuple = ()
print('list = [] 各元素的平方和为:', calc(list))
print('tuple = () 各元素的平方和为:', calc(tuple))
print('calc()的结果为:', calc())
'''
    #注：该种定义函数参数方式的缺点：#
    每次调用calc()的时候先要组装一个list或tuple，
    若将list或tuple中的每一个元素作为参数直接调用函数，函数的参数就变为可变参数
    形如：calc(nums[0], nums[1], nums[2]...)
    具体参考：func_def_param_test1.py
'''