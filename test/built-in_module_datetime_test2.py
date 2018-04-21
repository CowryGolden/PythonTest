#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：datetime-获取指定日期和时间
    # 使用场景：
        获取指定日期和时间
        要指定某个日期和时间，我们直接用参数构造一个datetime：


'''
# 获取指定日期和时间
from datetime import datetime

dt = datetime(2012, 12, 31, 12, 12)    # 用指定日期时间创建datetime
print('dt =', dt)    # dt = 2012-12-31 12:12:00

r'''
    #注：

'''