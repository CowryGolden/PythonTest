#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-使用元类：定义hello模块
    # 使用场景：
        动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
        比方说我们要定义一个Hello的class，就写一个hello.py模块：
'''
# 当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象，测试如下：
from hello import Hello

h = Hello()
h.hello()
print('type(Hello) =', type(Hello))
print('type(h) =', type(h))
'''
    输出结果：
        Hello, world
        type(Hello) = <class 'type'>
        type(h) = <class 'hello.Hello'>

    分析：type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
        *** 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
        *** type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
            具体例子参见：oop_advance_metaclass_type_test2.py
'''

'''
    #注：
    
'''