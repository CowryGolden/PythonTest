#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：itertools模块，groupby()把迭代器中相邻的重复元素挑出来放在一起
    # 使用场景：
        groupby()把迭代器中相邻的重复元素挑出来放在一起：
        如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：

'''
# groupby()把迭代器中相邻的重复元素挑出来放在一起，如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key，可以使用正则表达式：
import itertools

for key,group in itertools.groupby('AaaBbBcCAaaA', lambda c: c.upper()):
    print(key, list(group))

r'''
    #注：实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。

'''