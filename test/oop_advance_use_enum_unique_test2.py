#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-枚举类：Enum的使用，自定义枚举类（从Enum继承），使用@unique装饰器检查自定义枚举类中是否有重复值
    # 使用场景：
        Enum中的每个实例的value属性是枚举类自动赋给实例成员的int常量，默认从1开始计数。
        如果需要更精确地控制枚举类型或自定义实例成员的数据类型，可以从Enum派生出自定义类。
'''
# 自定义个星期枚举类（从Enum继承），周日为0，周一为1……周六为6，并使用@unique装饰器检查自定义枚举类中是否有重复值
from enum import Enum, unique

@unique    # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0    # Sun的value属性被锁定为0，不再是默认的1
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6    # 有重复值检查不通过（如果Sat = 5，将会报错：ValueError: duplicate values found in <enum 'Weekday'>: Sat -> Fri）

# 测试
day1 = Weekday.Mon
print('Weekday.Mon =', Weekday.Mon)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Sat.name =', Weekday.Sat.name)
print('Weekday.Mon.value =', Weekday.Mon.value)
print('day1 == Weekday.Mon :', day1 == Weekday.Mon)
print('day1 == Weekday.Tue :', day1 == Weekday.Tue)
print('Weekday(1) =', Weekday(1))
# print('Weekday(7) =', Weekday(7))    # 实例成员value属性不存在（或越界）报错：ValueError: 7 is not a valid Weekday
print('--------')
# 遍历Weekday
for name, member in Weekday.__members__.items():
    # print(name, '=>', member, '|', str(member) + '.value :', member.value)
    print('name=%s => member=%s | %s.value : %d' % (name, member, member, member.value))

# 从上面的测试可知：既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量的值。
'''
    #注：枚举类的每个实例成员都是常量；（若无自定义）枚举类默认给实例成员的value属性赋为int型，并且从1开始；
        若有自定义，则value为自定义数据类型和数值；
        Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
    
'''