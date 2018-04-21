#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：itertools模块，cycle()方法，会把传入的序列无限循环下去
    # 使用场景：
        Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
        首先，我们看看itertools提供的几个“无限”迭代器：count()会创建一个无限的迭代器
        cycle()会把传入的一个序列无限重复下去：

'''
# 使用itertools.cycle()把传入的一个序列无限重复下去：
import itertools

cs = itertools.cycle('ABC')    # 注意字符串也是序列的一种

for c in cs:
    print(c)

r'''
    #注：同样停不下来，只能按Ctrl+C退出。

'''