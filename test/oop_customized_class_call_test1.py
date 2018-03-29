#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-定制类：__call__()的使用
    # 使用场景：
        一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
        任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
'''
# 
class Student(object):
    def __init__(self, name):
        self.__name = name

    def __call__(self):
        print('My name is %s.' % self.__name)

s = Student('Michael')
s()
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
print('callable(Student()) =', callable(Student('Michael')))
print('callable(s) =', callable(s))
print('callable(max) =', callable(max))
print('callable([1,2,3]) =', callable([1,2,3]))
print('callable(None) =', callable(None))
print('callable(\'str\') =', callable('str'))

'''
    #注：通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
    
'''