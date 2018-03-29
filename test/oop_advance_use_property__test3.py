#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程：使用 @property     
'''
import time
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):
    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    #定义只读属性，只有get方法没有set方法
    @property
    def age(self):
        return int(time.localtime().tm_year) - self.__birth
# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

s = Student()
s.birth = 1988
print('s.birth =', s.birth)
print('s.age =', s.age)
# s.age = 29    # 报错：AttributeError: can't set attribute

'''
    #注：
   
'''