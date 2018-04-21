#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：itertools模块，count()方法创建一个无线迭代器，结合takewhile()函数控制无限序列的输出
    # 使用场景：
        无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
        无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：

'''
# 使用itertools.takewhile()控制无限无限序列的输出
import itertools

naturals = itertools.count(1)

ns = itertools.takewhile(lambda x: x <= 10, naturals)

print('list(ns) =', list(ns))

r'''
    #注：

'''