#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP-获取对象信息：instance()的使用
'''
# 继承关系：object -> Animal -> Dog -> Husky
class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print("isinstance(h, Husky) :", isinstance(h, Husky))       
print("isinstance(h, Dog) :", isinstance(h, Dog)) 
print("isinstance(h, Animal) :", isinstance(h, Animal))      
print("isinstance(h, Animal) and isinstance(h, Dog) :", isinstance(h, Animal) and isinstance(h, Dog))   
print("isinstance(d, Husky) :", isinstance(d, Husky))  

print('--------')
# 能有type()判断的基本数据类型也可以用isinstance()判断：
print("isinstance('a', str) :", isinstance('a', str))
print("isinstance(123, int) :", isinstance(123, int))
print("isinstance(b'a', bytes) :", isinstance(b'a', bytes))
# 还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print("isinstance([1, 2, 3], (list, tuple)) :", isinstance([1, 2, 3], (list, tuple)))
print("isinstance((1, 2, 3), (list, tuple)) :", isinstance((1, 2, 3), (list, tuple)))


'''
    #注：总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
'''