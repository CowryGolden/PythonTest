#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-高阶函数-filter练习：求回文数
'''
def is_palindrome(n):
    return str(n) == str(n)[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000的回文数为:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

'''
    #注：利用字符串的反转
'''