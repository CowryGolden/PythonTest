#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：datetime转换为timestamp
    # 使用场景：
        在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
        你可以认为：
            timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
        对应的北京时间是：
            timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
        可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
        这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。    
        把一个datetime类型转换为timestamp只需要简单调用timestamp()方法；

'''
# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
from datetime import datetime

dt = datetime(2018, 4, 16, 14, 36, 21, 787460)    # 用指定日期时间创建datetime
ts = dt.timestamp()    # 把datetime转换为timestamp
print('ts =', ts)    # ts = 1523860581.78746
print('type(ts) =', type(ts))    # type(ts) = <class 'float'>

r'''
    #注：注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
        某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

'''