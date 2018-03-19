#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 条件判断练习
# Python的if...elif...else很灵活。条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行。
# 练习题：小明身高1.75m，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
"""
	低于18.5：过轻
	18.5-25：正常
	25-28：过重
	28-32：肥胖
	高于32：严重肥胖
"""
height = 1.72
weight = 80.0

bmi = weight / (height * height)
if bmi < 18.5:
    print('BMI=%.2f %s' % (bmi,'过轻'))
elif bmi < 25:
    print('BMI=%.2f %s' % (bmi,'正常'))
elif bmi < 28:
    print('BMI=%.2f %s' % (bmi,'过重'))
elif bmi < 32:
    print('BMI=%.2f %s' % (bmi,'肥胖'))
else:
    print('BMI=%.2f %s' % (bmi,'严重肥胖'))
