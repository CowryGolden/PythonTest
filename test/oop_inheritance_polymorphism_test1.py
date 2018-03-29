#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP-继承和多态（inheritance and polymorphism）：继承练习
    # 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
'''
# 比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
class Animal(object):
    def run(self):
        print('Animal is running...')
# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
    pass

class Cat(Animal):
    pass    

# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
# 继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
dog = Dog()
dog.run()

cat = Cat()
cat.run()

'''
    #注：数据封装、继承和多态是面向对象的三大特点(encapsulation, inheritance and polymorphism)
'''