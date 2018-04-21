#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：timestamp转换为datetime
    # 使用场景：
        在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
        你可以认为：
            timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
        对应的北京时间是：
            timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
        可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
        这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。    
        把一个datetime类型转换为timestamp只需要简单调用timestamp()方法；
        要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法；

'''
# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
from datetime import datetime

ts = 1356927120.0
dt = datetime.fromtimestamp(ts)
print('dt =', dt)    # dt = 2012-12-31 12:12:00
print('type(dt) =', type(dt))    # type(dt) = <class 'datetime.datetime'>

# 注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
# timestamp也可以直接被转换到UTC标准时区的时间：
print('本地时间：dt =', dt) 
utc_dt = datetime.utcfromtimestamp(ts)
print('UTC时间：utc_dt =', utc_dt) 

r'''
    #注：注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
        本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：
            2012-12-31 12:12:00
        实际上就是UTC+8:00时区的时间：
            2012-12-31 12:12:00 UTC+8:00
        而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：
            2012-12-31 04:12:00 UTC+0:00         

'''