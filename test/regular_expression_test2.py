#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 正则表达式：练习
    # 使用场景：
        版本二可以提取出带名字的Email地址：
            <Tom Paris> tom@voyager.org => Tom Paris
            bob@example.com => bob

'''
# 提取带名字的email
import re

def name_of_email(addr):
    re_email = re.compile(r'^\<?([a-zA-Z\s]*?)\>?\s*?([a-zA-Z0-9\.]+)@([a-zA-Z0-9]+)\.([a-zA-Z]{2,3})$')  # 使用?非贪婪匹配
    # re_email = re.compile(r'<?([\w\s]+)>?([\w\s]*)(@[0-9a-zA-Z]+\.\w{2,3})')
    m = re_email.match(addr)    
    if m:
        print(re_email.match(addr).groups())    # 测试
        return m.group(1) or m.group(2)
    else:
        return None


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

r'''
    #注：

'''