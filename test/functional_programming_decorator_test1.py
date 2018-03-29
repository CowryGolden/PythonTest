#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-装饰器练习：在函数调用前打印日志（比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。）
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s() begin:' % func.__name__)
        return func(*args, **kw)
    return wrapper

#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2018-03-19')

#调用now()函数
now()

#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志;
#把@log放到now()函数的定义处，相当于执行了语句：now = log(now)

'''
    #注：函数对象有一个__name__属性，可以拿到函数的名字；
'''