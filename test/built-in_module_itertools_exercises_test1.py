#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：itertools模块练习
    # 使用场景：
        计算圆周率可以根据公式：
            pi/4=1-1/3+1/5-1/7+1/9……
            pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 + ...
        利用Python提供的itertools模块，我们来计算这个序列的前N项和：

'''
# 计算圆周率pi的值
import itertools

def pi(N):
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odds = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    nos = itertools.takewhile(lambda n: n <= 2*N-1, odds)
    L = list(nos)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # L1 = [4/L[i] if i % 2 == 0 else -4/L[i] for i in range(len(L))]
    L1 = [pow(-1, i)*(4/L[i]) for i in range(len(L))]
    # step 4: 求和:
    return sum(L1)
"""
def pi(N):
    oddList = itertools.count(1, 2)
    oddList_N = itertools.islice(oddList, 0, N)    # Return an iterator, islice(iterable, stop) --> islice object islice(iterable, start, stop[, step])
    a = itertools.islice(itertools.cycle([1, -1]), 0, N)    # 循环n个[1, -1]列表数
    unSignPiList = map(lambda x:4/x, oddList_N)
    signPiList = map(lambda x,y:x*y, unSignPiList, a)
    return sum(signPiList)
""" 
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
# print(pi(10000000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

r'''
    #注：

'''