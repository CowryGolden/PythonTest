#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP(Object Oriented Programming)：面向对象编程引入练习（与传统面向过程的比较）
'''
# 传统的使用函数（面向过程编程）
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

# 测试，调用函数
print_score(std1)
print_score(std2)

# 使用面向对象的编程方式
class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 创建对象并调用方法
bart = Student('Bart Sampson', 59)
lisa = Student('Lisa Sampson', 87)
bart.print_score()
lisa.print_score()     

'''
    #注：数据封装、继承和多态是面向对象的三大特点
'''