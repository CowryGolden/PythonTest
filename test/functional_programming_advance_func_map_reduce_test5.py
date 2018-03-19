#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-高阶函数-map/reduce练习：实现数字字符串转数字；（str2float）
'''
from functools import reduce

def str2float(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    nums = s.split('.') #以'.'作为分隔符，隔成整数部分和小数部分字符串数组
    if len(nums[0]) == 0:
        i = 0
    else:
        i = reduce(lambda x, y: x * 10 + y, map(lambda i: digits[i], nums[0])) #整数部分(将整数部分的数字字符串转为数值型)
    if len(nums) < 2:
        return i + 0.0
    else:
        f = reduce(lambda x, y: x * 0.1 + y, map(lambda i: digits[i], nums[1][::-1]), 0.0) * 0.1 #小数部分(将小数部分的数字字符串转为数值型)
    return i + f

print("str2float('0') =", str2float('0'))
print("str2float('123.456') =", str2float('123.456'))
print("str2float('123.45600') =", str2float('123.45600'))
print("str2float('0.1234') =", str2float('0.1234'))
print("str2float('.1234') =", str2float('.1234'))
print("str2float('120.0034') =", str2float('120.0034'))

#测试
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

'''
    #注：
'''