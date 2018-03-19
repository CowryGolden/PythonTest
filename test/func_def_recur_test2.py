#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 自定义递归函数练习：求 n! = 1 x 2 x 3 x ... x n  
    # 要求：改为尾递归模式；尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
        func_def_recur_test1.py中的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
'''

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print('fact(10) =', fact(10))
print('fact(20) =', fact(20))
print('fact(50) =', fact(50))
print('fact(100) =', fact(100))
'''
    #注：解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
    尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
'''