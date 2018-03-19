#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# while循环中continue语句的使用；continue语句跳出当前循环的本次循环，直接开始下一次循环；
# 例如：打印1~20间奇数

n = 0
while n < 20:
    n = n + 1
    if n % 2 == 0: # 当n是偶数时，条件满足，执行如下continue语句
        continue # continue语句会跳出当前循环的本次循环，本次循环的后续print语句不会执行，直接进入下一次循环
    print(n)	
print('END') # 打印完成后，紧接着打印END，程序结束。