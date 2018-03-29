#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP(Object Oriented Programming)：面向对象编程练习
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 75:
            return 'B'
        elif self.score >= 60:
            return 'C'    
        else:
            return 'D'
 
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

'''
    #注：数据封装、继承和多态是面向对象的三大特点
'''