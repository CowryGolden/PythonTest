#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：contextlib模块的closing()的使用
    # 使用场景：
        如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。
        closing()的作用就是把任意对象变为上下文对象，并支持with语句。
        例如，用with语句使用urlopen()：

'''
# 用with语句使用urlopen()：
from contextlib import closing
from urllib.request import urlopen
import ssl

# with closing(urlopen('https://www.python.org', context=ssl._create_unverified_context())) as page:
with closing(urlopen('https://www.python.org')) as page:    # 如果要爬去https的需要导入ssl，然后设置context=ssl._create_unverified_context()
    for line in page:
        print(line)


r'''
    #注：closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
            @contextmanager
            def closing(thing):
                try:
                    yield thing
                finally:
                    thing.close()    
        它的作用就是把任意对象变为上下文对象，并支持with语句。


'''