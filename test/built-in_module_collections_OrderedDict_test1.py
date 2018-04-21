#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块-collections集合模块：OrderedDict的使用
    # 使用场景：
        使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
        如果要保持Key的顺序，可以用OrderedDict；
        注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序；

'''
# 使用OrderedDict对dict的key排序（只能按插入顺序排序）
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print('d =', d)    # dict的Key是无序的
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print('od1 =', od1)    # OrderedDict的Key是有序的

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print('od =', od)    # 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

r'''
    #注：注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序；

'''