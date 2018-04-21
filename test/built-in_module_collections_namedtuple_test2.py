#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块-collections集合模块：namedtuple的使用
    # 使用场景：
        我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
            >>> p = (1, 2)        
        但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
        定义一个class又小题大做了，这时，namedtuple就派上了用场；
        namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
        这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。 
            使用方法：namedtuple('名称', [属性list])

'''
# 使用namedtuple定义一个圆心坐标及半径的圆
from collections import namedtuple

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 2, 2)

print('c.x =', c.x)
print('c.y =', c.y)
print('c.r =', c.r)

r'''
    #注：

'''