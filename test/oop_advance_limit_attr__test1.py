#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程：实例属性的动态绑定
    正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
'''
# 先定义class：
class Student(object):
    pass

s = Student()    
# 然后，尝试给实例绑定一个属性：
print('给实例s动态绑定一个属性name：')
s.name = 'Michael'
print('给Student类的实例s动态绑定的属性name为：', s.name)
# 还可以尝试给实例绑定一个方法，下面定义个设置年龄的方法：
def set_age(self, age):
    self.age = age

from types import MethodType
print('给Student类的实例s动态绑定一个方法：set_age')
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
print('调用实例s的set_age方法，设置年龄')
s.set_age(25)   # 调用实例方法
print('测试调用结果：s.age =', s.age)

print('--------')
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
print('---- 给一个实例绑定的方法，对另一个实例是不起作用的 ----')
print('重新定义一个Student类的实例s1：')
s1 = Student()
print('尝试使用实例s1调用给实例s动态绑定的方法set_age，设置年龄')
if hasattr(s1, 'set_age'):
    s1.set_age(26) 
else:
    print('实例s1调用给实例s动态绑定的方法set_age失败！！！')

print('--------') 
print('---- 为了给所有实例都绑定方法，可以给class绑定方法 ----')
print('给类Student绑定一个set_score方法，让所有实例都可以访问该方法')
def set_score(self, score):
    self.score = score
# 给class Student绑定set_score方法    
Student.set_score = set_score
# 给class绑定方法后，所有实例均可调用：
print('实例s调用类Student的set_score方法，设置分数')
s.set_score(100)
print('测试调用结果：s.score =', s.score)
print('实例s1调用类Student的set_score方法，设置分数')
s1.set_score(98)
print('测试调用结果：s1.score =', s1.score)

'''
    #注：通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
    但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。参加oop_advance_limit_attr__test2.py详解
   
'''