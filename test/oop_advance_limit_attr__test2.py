#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程：使用 __slots__ 来限制该class实例能添加的属性
'''
# 只允许对Student实例添加name和age属性。为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性name
s.age = 25 # 绑定属性age
print('测试属性name绑定结果：s.name =', s.name)
print('测试属性age绑定结果：s.age =', s.age)
try:
    s.score = 99
except AttributeError:
    print("类Student的实例s绑定属性score失败！！！'Student' object has no attribute 'score'") 
else:
    print("类Student的实例s绑定属性score成功！！！")
    print('测试属性score绑定结果：s.score =', s.score)

'''
# 原因分析：
    由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
    使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
'''
# 定义Student类的子类GraduateStudent，验证__slots__定义的属性仅对父类Student的实例起作用，对继承的子类是不起作用
class GraduateStudent(Student):
    pass

g = GraduateStudent()
try:
    g.score = 88  # 父类__slots__对其子类不起作用，仍能绑定属性成功
except AttributeError:
    print("类GraduateStudent的实例g绑定属性score失败！！！'GraduateStudent' object has no attribute 'score'") 
else:
    print("类GraduateStudent的实例g绑定属性score成功！！！")
    print('测试属性score绑定结果：g.score =', g.score)    
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。    
# 重新定义子类EnrollStudent，并且定义自身的__slots__
class EnrollStudent(Student):
    __slots__ = ('score')  # 在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

e  = EnrollStudent()

e.name = 'John'  # 绑定属性name
e.age = 22 # 绑定属性age
print('测试属性name绑定结果：e.name =', e.name)
print('测试属性age绑定结果：e.age =', e.age)

try:
    e.score = 60
except AttributeError:
    print("类EnrollStudent的实例e绑定属性score失败！！！'EnrollStudent' object has no attribute 'score'") 
else:
    print("类EnrollStudent的实例e绑定属性score成功！！！")
    print('测试属性score绑定结果：e.score =', e.score)   

try:
    e.gender = 'Female'
except AttributeError:
    print("类EnrollStudent的实例e绑定属性gender失败！！！'EnrollStudent' object has no attribute 'gender'") 
else:
    print("类EnrollStudent的实例e绑定属性gender成功！！！")
    print('测试属性gender绑定结果：e.gender =', e.gender)       

'''
    #注：
   
'''