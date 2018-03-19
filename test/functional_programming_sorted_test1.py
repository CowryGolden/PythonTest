#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-高阶函数-sorted练习：字母和数字排序
'''
from operator import itemgetter

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0].lower()

print('sorted(L, key=by_name) =', sorted(L, key=by_name))
print('sorted(L, key=itemgetter(0)) =', sorted(L, key=itemgetter(0)))

#再按成绩从高到低排序：
def by_score(t):
    return t[1] #return -t[1] #不使用key=reverse时用此

print('sorted(L, key=by_score) =', sorted(L, key=by_score, reverse=True))

'''
    #注：
'''