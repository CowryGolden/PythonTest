#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程：使用 __slots__ 来限制该class实例能添加的属性。课后练习
'''
# 用MethodType将方法绑定到类，并不是将这个方法直接写到内部类，而是在内存中创建了一个link指向外部方法，在创建实例的时候这个link也会被复制       
from types import MethodType
class Student(object):
    # __slots__ 只对类实例动态绑定属性方法受限制，但对class动态绑定属性方法不受限制！！！
    # __slots__ = ('name', 'age', 'a', 'b')    # 如果在slots中不限制add方法的绑定定义，在类实例绑定该方法时会报错：AttributeError: 'Student' object has no attribute 'add'
    __slots__ = ('name', 'age', 'a', 'b', 'add')
    pass

def add(self, a, b):
    self.a = a
    self.b = b
    return self.a + self.b

# 实例初始化
s = Student()

# 给实例绑定方法
s.add = MethodType(add, s) 
print('s.add(25, 10) =', s.add(25, 10))
#s.add = add    # s.add = add把add函数赋给了s.add；s.add(s,25,10)这个相当于调用add这个函数，其实就是add(s,25,10)
#print('s.add(s, 25, 10) =', s.add(s, 25, 10))  # 也可以写作：print('add(s, 25, 10) =', add(s, 25, 10))
print('s.a =', s.a)
print('s.b =', s.b)

# 给类绑定方法（# __slots__ 只对类实例动态绑定属性方法受限制，但对class动态绑定属性方法不受限制！！！也就是说，即使上面slots中没有限制add方法，下面也照样课可以绑定成功）
#Student.add = MethodType(add, Student)  # 与下面绑定方法相同
Student.add = add
s1 = Student()
print('s1.add(13, 17) =', s1.add(13, 17))

'''
    #注：__slots__ 只对类实例动态绑定属性方法受限制，但对class动态绑定属性方法不受限制！！！
   
'''