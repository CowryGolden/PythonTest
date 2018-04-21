#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：本地时间转换为UTC时间
    # 使用场景：
        本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
        一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：

'''
# 本地时间转换为UTC时间
from datetime import datetime, timedelta, timezone

tz_utc_8 = timezone(timedelta(hours=8))    # 创建时区UTC+8:00
now = datetime.now()
print('now =', now)    # now = 2018-04-16 16:00:41.467512
dt = now.replace(tzinfo=tz_utc_8)    # 强制设置为UTC+8:00
print('dt =', dt)    # dt = 2018-04-16 16:00:41.467512+08:00

r'''
    #注：如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。

'''