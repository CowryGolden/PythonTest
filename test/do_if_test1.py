#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
age = int(input('Input your age: '))

if age >= 18:
    print('Your age is %2d, you are an %s.' % (age,'adult'))
elif age >= 6:
    print('Your age is %2d, you are a %s.' % (age,'teenager'))
else:
    print('Your age is %2d, you are a %s.' % (age,'kid'))