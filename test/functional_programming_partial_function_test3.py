#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-偏函数练习：利用偏函数求和

'''
import functools

def add1(x, y = 2, z = 4):
    s = x + y + z
    return s

kw = {'y' : 4, 'z' : 16}
add2 = functools.partial(add1, **kw)

print('add1(1) =', add1(1))
print('add1(1, 3) =', add1(1, 3))
print('add1(1, 3, 5) =', add1(1, 3, 5))
print('add2(1) =', add2(1))
print('add2(1, y=3) =', add2(1, y=3))
print('add2(1, y=3, z=5) =', add2(1, y=3, z=5))

'''
    #注：
'''