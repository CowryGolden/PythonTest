#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：datetime加减
    # 使用场景：
        对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类

'''
# datetime加减
from datetime import datetime, timedelta    # delta 希腊字母δ，[数]变量增量 

now = datetime.now()

print('now =', now)
now1 = now + timedelta(hours=10)    # 在当前时间基础上增加10个小时
print('now1 =', now1)
now2 = now - timedelta(days=1)    # 在当前回见基础上减去1天
print('now2 =', now2)
now3 = now + timedelta(days=2, hours=12)    # 在当前时间基础上增加2天12个小时
print('now3 =', now3)

r'''
    #注：可见，使用timedelta可以很容易地算出前几天和后几天的时刻

'''