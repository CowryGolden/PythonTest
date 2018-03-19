#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n -2
print(sum)
