#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP(Object Oriented Programming)：面向对象编程练习
'''
class Person(object):
    # 这里就是初始化你将要创建的实例的属性
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
    
    # 定义你将要创建的实例所有用的技能
    def paoniu(self):
        print('%s，你拥有泡妞的技能' % self.name)   

    def eat(self):
        print('%s, You can eat something.' % self.name)     

# 开始创建实例
zhangsan = Person('张三',170, 56, 28)
lisi = Person('李四',175, 60, 30)

# 实例调用它的技能（方法）
zhangsan.paoniu()
lisi.eat()


'''
    #注：数据封装、继承和多态是面向对象的三大特点
'''