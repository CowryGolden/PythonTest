#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-匿名函数练习：改造成匿名函数
'''
#原始功能写法
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print('定义求奇数的函数：', L)
#匿名函数写法
print('anonymous function:',list(filter(lambda x: x%2==1, range(1,20))))
'''
    #注：关键字lambda表示匿名函数，冒号前面的x表示函数参数。
'''