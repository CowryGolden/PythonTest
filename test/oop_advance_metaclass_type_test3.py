#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-使用元类：metaclass的使用
    # 使用场景：
        类创建顺序：先定义metaclass，就可以创建类，最后创建实例。metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
        metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
        我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
'''
# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
# metaclass是类的模板，所以必须从'type'类派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass = ListMetaclass):
    pass
# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
'''    
# __new__()方法接收到的参数依次是：
    1、当前准备创建的类的对象；
    2、类的名字；
    3、类继承的父类集合tuple元组；
    4、类的方法集合。    
'''
# 测试一下MyList是否可以调用add()方法：
L = MyList()
L.add(1)
L.add(2)
L.add(3)
print('L =', L)
'''
# 而普通的list没有add()方法：
    >>> L2 = list()
    >>> L2.add(1)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'list' object has no attribute 'add'
'''

'''
    #注：
'''