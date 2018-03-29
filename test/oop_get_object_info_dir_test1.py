#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP-获取对象信息：dir()的使用，以及hasattr(),getattr(),setattr()等方法的使用
    如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法，例如：
    >>> dir('ABC')
    ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
    
    类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
    >>> len('ABC')
    3
    >>> 'ABC'.__len__()
    3

'''
# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x    

obj = MyObject()

print("hasattr(obj, 'x') :", hasattr(obj, 'x'))    # 有属性'x'吗？
print("obj.x :", obj.x)    # 获取属性'x'
print("hasattr(obj, 'y') :", hasattr(obj, 'y'))    # 有属性'y'吗？
setattr(obj, 'y', 19)    # 设置一个属性'y'
print("hasattr(obj, 'y') :", hasattr(obj, 'y'))    # 有属性'y'吗？
print("getattr(obj, 'y') :", getattr(obj, 'y'))    # 获取属性'y'
print("obj.y :", obj.y)    # 获取属性'y'
# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# 可以传入一个default参数，如果属性不存在，就返回默认值：
print("getattr(obj, 'z', 404) :", getattr(obj, 'z', 404))    # 获取属性'z'，如果不存在，返回默认值404

print('--------')
# 也可以获得对象的方法：
print("hasattr(obj, 'power') :", hasattr(obj, 'power'))    # 有属性'power'吗？
print("getattr(obj, 'power') :", getattr(obj, 'power'))    # 获取属性'power'
fn = getattr(obj, 'power')    # 获取属性'power'并赋值到变量fn
print("fn = getattr(obj, 'power') :", fn)    # fn指向obj.power
print("fn() :", fn())    # 调用fn()与调用obj.power()是一样的


'''
    #注：如果试图获取不存在的属性，会抛出AttributeError的错误：
    >>> getattr(obj, 'z') # 获取属性'z'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'MyObject' object has no attribute 'z'
'''