#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：contextlib模块的@contextmanager装饰器使用
    # 使用场景：
        很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。

'''
# 在某段代码执行前后自动执行特定代码，用@contextmanager实现
from contextlib import contextmanager

@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('h1'):
    print('Hello')
    print('World')

r'''
    #注：以上代码执行结果为：
            <h1>
            Hello
            World
            </h1>    
        代码的执行顺序是：
            1、with语句首先执行yield之前的语句，因此打印出<h1>；
            2、yield调用会执行with语句内部的所有语句，因此打印出Hello和World；
            3、最后执行yield之后的语句，打印出</h1>。                

'''