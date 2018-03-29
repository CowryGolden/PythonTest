#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程：使用 @property     
'''
'''
# 先导引入：
    oop_advance_use_property__test1.py中的调用方法又略显复杂，没有直接用属性这么直接简单。
    有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！
    还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的。
'''
class Student(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if (value < 0 or value > 100):
            raise ValueError('score must between 0 and 100!')
        self.__score = value
# 现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：
s = Student()
s.score = 60   # OK，实际转化为s.set_score(60)
print('s.score =', s.score)    # OK，实际转化为s.get_score()
# s.score = 'a' #报错！！          
s.score = 9999 #报错！！
# print('s.score =', s.score)  


'''
    #注：@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    # 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性可能不是直接暴露的，而是通过setter和getter方法来实现的。
   
'''