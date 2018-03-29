#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-定制类：__str__()的使用
'''
# 先导引入，我们先定义一个Student类，打印一个实例：
'''
class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael'))
'''
# 打印出一堆：<__main__.Student object at 0x000000F5F3D38518>，不好看出结果
# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：
'''
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name : %s)' % self.name    

print(Student('Michael'))
'''
# 这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。
# 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：
'''
    >>> s = Student('Michael')
    >>> s
    <__main__.Student object at 0x109afb310>
'''
#这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
#解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name : %s)' % self.name

    __repr__ = __str__

#通过上述改造后，在终端控制台调试时输出s时，就会输出比较好看的字符串
print(Student('Michael'))

'''
    #注：
'''