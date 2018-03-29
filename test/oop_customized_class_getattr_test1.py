#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-定制类：__getattr__()的使用
    # 使用场景：
        正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
            class Student(object):
                def __init__(self):
                    self.name = 'Michael'

            >>> s = Student()
            >>> print(s.name)
            Michael
            >>> print(s.score)
            Traceback (most recent call last):
            ...
            AttributeError: 'Student' object has no attribute 'score'
        错误信息很清楚地告诉我们，没有找到score这个attribute。
        要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。    
'''
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
    def __getattr__(self, attr):
        if attr=='score':  # 调用方式：s.score
            return 99
        if attr=='age':  # 调用方式：s.age()【由于返回为lambda表达式】
            return lambda: 25

        # 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
        raise AttributeError("'Student' object has no attribute '%s'" % attr)

# 测试
s = Student()
print('s.name =', s.name)
print('s.score =', s.score)
print('s.age() =', s.age())  # 由于属性age返回lambda表达式，因此调用按函数方式调用
print('s.abc =', s.abc)   # 由于定义的__getattr__默认返回就是None，由于控制了属性找不到返回为None时抛出AttributeError的错误；因此该语句抛异常

'''
    #注：注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
        以上的处理方式实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
        这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。（具体例子参见：oop_customized_class_getattr_test2.py）
        举个例子：
            现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
                http://api.server/user/friends
                http://api.server/user/timeline/list
            如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
            利用完全动态的__getattr__，我们可以写出一个链式调用：    
    
'''