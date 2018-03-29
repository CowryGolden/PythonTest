#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-装饰器练习：请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

    再思考一下能否写出一个@log的decorator，使它既支持：
    @log
    def f():
        pass
    又支持：
    @log('execute')
    def f():
        pass
'''
import time, functools

def log(*text, **fk):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            start_time = time.time()
            print('%s() begins to be called' % (func.__name__))
            fn = func(*args, **kw)
            print('%s() ends to be called' % (func.__name__))
            end_time = time.time()
            if text == ():
                print('%s() in %.4f ms' % (func.__name__, (end_time - start_time)))
            else:
                print('%s %s() in %.4f ms' % (text[0], func.__name__, (end_time - start_time)))
            return fn
        return wrapper
    return decorator


# 测试
@log()
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@log('execute')
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