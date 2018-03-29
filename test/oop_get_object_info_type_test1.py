#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP-获取对象信息：type()的使用
'''
import types

# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 首先，我们来判断对象类型，使用type()函数，基本类型都可以用type()判断：
print('type(123)==type(456) :', type(123)==type(456))
print('type(123)==int :', type(123)==int)
print("type('abc')==type('123') :", type('abc')==type('123'))
print("type('abc')==str :", type('abc')==str)
print("type('abc')==type(123) :", type('abc')==type(123))

def fn():
    pass

# 判断一个对象是否是函数
print("type(fn)==types.FunctionType :", type(fn)==types.FunctionType)
print("type(abs)==types.BuiltinFunctionType :", type(abs)==types.BuiltinFunctionType)
print("type(lambda x: x)==types.LambdaType :", type(lambda x: x)==types.LambdaType)
print("type((x for x in range(10)))==types.GeneratorType :", type((x for x in range(10)))==types.GeneratorType)


'''
    #注：基本类型都可以用type()判断：
        >>> type(123)
        <class 'int'>
        >>> type('str')
        <class 'str'>
        >>> type(None)
        <type(None) 'NoneType'>

        >>> type(abs)
        <class 'builtin_function_or_method'>
        >>> type(a)
        <class '__main__.Animal'>
'''