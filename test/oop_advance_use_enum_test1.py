#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-枚举类：Enum的使用
    # 使用场景：
        当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
            JAN = 1
            FEB = 2
            MAR = 3
            ...
            NOV = 11
            DEC = 12
        好处是简单，缺点是类型是int，并且仍然是变量。
        更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
'''
# 实现一个月份枚举类
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
print('Month.Jan.name =', Month.Jan.name)
print('Month.Jun.value =', Month.Jun.value)
print('Month.Aug =', Month.Aug)
print('Month.__members__[\'Dec\'] =', Month.__members__['Dec'])
print('Month(1) =', Month(1))    # 枚举类的每个实例成员都是常量；（若无自定义）枚举类默认给实例成员的value属性赋为int型，并且从1开始；
print('Month(1).value =', Month(1).value)

# 枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

'''
    #注：value属性则是自动赋给成员的int常量，默认从1开始计数。

执行结果：
Month.Jan.name = Jan
Month.Jun.value = 6
Month.Aug = Month.Aug
Month.__members__['Dec'] = Month.Dec
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
Apr => Month.Apr , 4
May => Month.May , 5
Jun => Month.Jun , 6
Jul => Month.Jul , 7
Aug => Month.Aug , 8
Sep => Month.Sep , 9
Oct => Month.Oct , 10
Nov => Month.Nov , 11
Dec => Month.Dec , 12    
'''