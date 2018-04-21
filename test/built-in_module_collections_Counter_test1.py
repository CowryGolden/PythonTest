#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块-collections集合模块：Counter的使用
    # 使用场景：
        Counter是一个简单的计数器，例如，统计字符出现的个数；
        Counter实际上也是dict的一个子类；
'''
# 统计字符串中字符出现的个数
from collections import Counter

counter = Counter()

for ch in 'programming':
    counter[ch] += 1

print('counter =', counter)    # 结果：counter = Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
print('isinstance(counter, dict) =', isinstance(counter, dict))    # True
print('字母r出现的次数为 :', counter['r'])

r'''
    #注：Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。

'''