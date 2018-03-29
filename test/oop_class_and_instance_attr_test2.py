#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP-实例属性和类属性：类属性使用练习；
    题目描述：为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
'''
# 
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Student\'s count:', Student.count)
            print('测试通过!')

'''
    #注：
    总结：
        1、实例属性属于各个实例所有，互不干扰；
        2、类属性属于类所有，所有实例共享一个属性；
        3、不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''