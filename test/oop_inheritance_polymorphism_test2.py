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
# 当然，子类可以对父类方法进行重写，也可以对子类增加一些方法，比如Dog类：
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    
    def eat(self):
        print('Dog is eating meat...')

# 对父类run方法进行重写
class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

'''
    #注：数据封装、继承和多态是面向对象的三大特点(encapsulation, inheritance and polymorphism)
    #分析：当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
    （具体如何理解多态，参见：oop_inheritance_polymorphism_test3.py）
'''