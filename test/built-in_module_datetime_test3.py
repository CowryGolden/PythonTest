#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：datetime模块综合练习
    # 使用场景：
        题目要求：
        假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

'''
# 根据用户输入的日期时间字符串和时区信息字符串，编写函数将其转为timestamp
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    reg = re.match(r'UTC([\+\-][\d]{1,2})\:([\d]{2})', tz_str) 
    if reg:
        hours = int(reg.group(1))    # 时区匹配正则表达式时获取时区的数值
        print('hours =', hours)
        tz = timezone(timedelta(hours=hours))    # 创建时区
        dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')    # 将用户输入的日期时间str转换为datetime
        print('dt =', dt)
        tz_dt = dt.replace(tzinfo=tz)    # 将用户输入的日期时间强制设置到输入的时区
        print('tz_dt =', tz_dt)
        ts = tz_dt.timestamp()    # 将强制转为带时区时间的datetime转为timestamp
        print('ts =', ts)
        return ts
    else:
        return None

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

r'''
    #注：

'''