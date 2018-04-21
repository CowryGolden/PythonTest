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
# 使用namedtuple定义点坐标
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print('p =', p)
print('p.x =', p.x)    # 通过属性访问元素
print('p.y =', p.y)    # 通过属性访问元素

print('isinstance(p, Point) =', isinstance(p, Point))
print('isinstance(p, tuple) =', isinstance(p, tuple))
# 以上可以验证Point是tuple的一种子类，因此同样具备tuple的不变性
print('p[0] =', p[0])    # 由于为tuple的子类，因此可以通过索引访问属性，不过失去其优势
print('p[1] =', p[1])    # 由于为tuple的子类，因此可以通过索引访问属性，不过失去其优势

r'''
    #注：

'''