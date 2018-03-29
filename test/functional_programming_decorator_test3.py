#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-装饰器练习：在函数调用前打印日志（比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。）
'''

'''
functional_programming_decorator_test1.py 和 functional_programming_decorator_test2.py
以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
>>> now.__name__
'wrapper'
因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法参见：functional_programming_decorator_test3.py
'''
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#这个3层嵌套的decorator用法如下：
@log('execute')
def now():
    print('2018-03-19')

#调用now()函数
now()

'''
    #注：函数对象有一个__name__属性，可以拿到函数的名字；
'''