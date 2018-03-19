#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-高阶函数-map/reduce练习：使用map(func,Iterable)函数实现列表每个元素求平方再输出
'''
def f(x):
    return x * x

m = map(f, [1,2,3,4,5,6,7,8,9])

print(list(m))

#解释：map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

'''
    #注：map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''