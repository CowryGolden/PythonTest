#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# while循环中break语句的使用；break语句退出当前循环；
# 例如：打印1~100间前10个数

n = 1
while n <= 100:
    if n > 10: # 当n=11时，条件满足，执行如下break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END') # 打印出1~10后，紧接着打印END，程序结束。