#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-使用元类：定义hello模块
    # 使用场景：
        动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
        比方说我们要定义一个Hello的class，就写一个hello.py模块：
'''
# 定义hello模块的Hello类
class Hello(object):
    def hello(self, name = 'world'):
        print('Hello, %s.' % name)

'''
    #注：当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对
    
'''