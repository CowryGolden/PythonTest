#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块-collections集合模块：OrderedDict的使用
    # 使用场景：
        使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
        如果要保持Key的顺序，可以用OrderedDict；
        注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序；

'''
# 使用OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        # print('containsKey =', containsKey)
        # print('len(self) =', len(self))
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))   
        OrderedDict.__setitem__(self, key, value)             

d = LastUpdatedOrderedDict(3)

d['a'] = 1
d['b'] = 2
d['c'] = 3
print('d =', d)
d['x'] = 9
print('d =', d)

r'''
    #注：

'''