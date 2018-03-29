#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-装饰器练习：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
'''
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        f = fn(*args, **kw)
        end_time = time.time()
        print('%s executed in %.4f ms' % (fn.__name__, (end_time - start_time)))
        return f
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f == 33:
    print('fast(11, 22) =', f, '测试成功!')
else:
    print('测试失败!')
if s == 7986:
    print('slow(11, 22, 33) =', s, '测试成功!')
else:
    print('测试失败!')


'''
    #注：函数对象有一个__name__属性，可以拿到函数的名字；time模块可以获取系统当前时间
'''