#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：itertools模块，count()方法，创建一个无线迭代器
    # 使用场景：
        Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
        首先，我们看看itertools提供的几个“无限”迭代器：count()会创建一个无限的迭代器

'''
# 使用itertools.count()创建一个无限迭代器
import itertools

naturals = itertools.count(1, 2)    # count(start, step)

for n in naturals:
    print(n)

r'''
    #注：因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。

'''