#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：datetime-获取系统当前日期和时间
    # 使用场景：
        Python之所以自称“batteries included”，就是因为内置了许多非常有用的模块，无需额外安装和配置，即可直接使用。
        datetime是Python处理日期和时间的标准库。

'''
# 获取当前日期和时间
from datetime import datetime

now = datetime.now()
print('now =', now)

print('type(now) =', type(now))

r'''
    #注：注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
        如果仅导入import datetime，则必须引用全名datetime.datetime。
        datetime.now()返回当前日期和时间，其类型是datetime。

'''