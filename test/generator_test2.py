#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 生成器练习：使用generator实现斐波那契数列(Fibonacci)；generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
    eg：1,1,2,3,5,8,13,21,34,...
    分析：斐波那契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：下面先用函数方式实现
'''
def fib(max): # max表示最大生成斐波那契数列个数
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b # 相当于 t=(b, a+b); a = t[0]; b = t[1];
        n = n + 1
    return 'done'

print('fib(10) is', fib(10))
'''
    #注：使用generator方式实现参见：generator_test3.py
'''