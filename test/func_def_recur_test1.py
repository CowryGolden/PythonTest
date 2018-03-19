#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 自定义递归函数练习：求 n! = 1 x 2 x 3 x ... x n    
'''

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))
print('fact(100) =', fact(100))

'''
    #注：
'''