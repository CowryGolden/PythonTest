#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：str转换为datetime
    # 使用场景：
        很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。
        转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：

'''
# str转换为datetime，转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
from datetime import datetime

cday = datetime.strptime('2018-4-1 18:19:59', '%Y-%m-%d %H:%M:%S')    # str parse time
print('cday =', cday)  # cday = 2018-04-01 18:19:59
print('type(cday) =', type(cday))  # type(cday) = <class 'datetime.datetime'>

r'''
    #注：字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。详细的说明请参考Python文档[https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior]。
        注意转换后的datetime是没有时区信息的，默认是指当前操作系统设定的时区。

'''