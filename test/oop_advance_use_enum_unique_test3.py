#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-枚举类：Enum的使用，自定义枚举类（从Enum继承），使用@unique装饰器检查自定义枚举类中是否有重复值
    # 使用场景：
        Enum中的每个实例的value属性是枚举类自动赋给实例成员的int常量，默认从1开始计数。
        如果需要更精确地控制枚举类型或自定义实例成员的数据类型，可以从Enum派生出自定义类。
'''
# 练习，把Student的gender属性改造为枚举类型，可以避免使用字符串：
from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = Gender(gender)

# 测试:
bart = Student('Bart', Gender.Male)
print('isinstance(Gender.Male, Enum) =', isinstance(Gender.Male, Enum))
print('isinstance(bart.gender, Enum) =', isinstance(bart.gender, Enum))
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


'''
    #注：枚举类的每个实例成员都是常量；（若无自定义）枚举类默认给实例成员的value属性赋为int型，并且从1开始；
        若有自定义，则value为自定义数据类型和数值；
        Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
    
'''