#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：itertools模块，groupby()把迭代器中相邻的重复元素挑出来放在一起
    # 使用场景：
        groupby()把迭代器中相邻的重复元素挑出来放在一起：

'''
# groupby()把迭代器中相邻的重复元素挑出来放在一起：
import itertools

for key,group in itertools.groupby('AAABBBCCAAAA'):
    print(key, list(group))

r'''
    #注：实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。

'''