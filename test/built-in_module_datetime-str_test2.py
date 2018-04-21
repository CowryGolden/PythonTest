#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：datetime转换为str
    # 使用场景：
        很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。
        转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串；
        如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：

'''
# datetime转换为str，转换方法是通过datetime.strftime()实现，需要一个日期和时间的格式化字符串：
from datetime import datetime

now = datetime.now()
now_str = now.strftime('%Y-%m(%b/%B)-%d %a(%A) (%x) %H:%M')    # str format time

print('now_str =', now_str)    # now_str = 2018-04(Apr/April)-16 Mon(Monday) (04/16/18) 15:27
print('type(now_str) =', type(now_str))    # type(now_str) = <class 'str'>

r'''
    #注：字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。详细的说明请参考Python文档[https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior]。
        
'''