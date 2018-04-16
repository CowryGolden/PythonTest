#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 正则表达式：re模块split练习
    # 使用场景：
        用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：

'''
# re模块的使用
import re

s1 = 'a b   c'

list1 = s1.split(' ')
print('list1 =', list1)  # 输出结果：list1 = ['a', 'b', '', '', 'c']

# 以上方法无法识别连续的空格，用正则表达式试试：
list2 = re.split(r'\s+', s1)
print('list2 =', list2)  # 输出结果：list2 = ['a', 'b', 'c']

# 以上方法无论多少个空格都可以正常分割。加入,试试：
s2 = 'a,b, c  d'
list3 = re.split(r'[\s\,]+', s2)
print('list3 =', list3)  # 输出结果：list3 = ['a', 'b', 'c', 'd']

#再加入;试试：
s3 = 'a,b;; c  d'
list4 = re.split(r'[\s\,\;]+', s3)
print('list4 =', list4)  # 输出结果：list4 = ['a', 'b', 'c', 'd']

r'''
    #注：

'''