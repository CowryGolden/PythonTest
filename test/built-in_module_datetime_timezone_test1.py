#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：时区转换
    # 使用场景：
        我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：

'''
# 时区转换
from datetime import datetime, timedelta, timezone

# 拿到UTC时间并强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('utc_dt =', utc_dt)
# 使用datetime的astimezone()方法将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('bj_dt =', bj_dt)
# 使用datetime的astimezone()方法将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt =', tokyo_dt)
# 使用datetime的astimezone()方法将北京时间转为东京时间
tokyo_dt1 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt1 =', tokyo_dt1)

r'''
    #注：时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
        利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
        特别注意：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt1的转换。

        小结：
            1、datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
            2、如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

'''