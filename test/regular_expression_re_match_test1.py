#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 正则表达式：re模块match练习
    # 使用场景：
        Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意：
            s = 'ABC\\-001' # Python的字符串
            # 对应的正则表达式字符串变成：
            # 'ABC\-001'     
        因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
            s = r'ABC\-001' # Python的字符串
            # 对应的正则表达式字符串不变：
            # 'ABC\-001'            

'''
# re模块的使用
import re
# test = '010-12345'
# test = '010   12345'
test = '010*12345'
m = re.match(r'^\d{3}[\-\s]+\d{3,8}$', test)
if m:
    print('OK')
else:
    print('Failed')

r'''
    #注：

'''