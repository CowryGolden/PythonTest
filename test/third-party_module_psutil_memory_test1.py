#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用第三方模块-psutil：psutil模块获取内存信息
    # 使用场景：
        使用psutil模块的*_memory相关方法获取内存信息

'''
# 使用psutil模块的*_memory相关方法获取内存信息
import psutil

print('psutil.virtual_memory() =', psutil.virtual_memory())
# 输出结果：psutil.virtual_memory() = svmem(total=8452730880, available=4860084224, percent=42.5, used=3592646656, free=4860084224)

print('psutil.swap_memory()', psutil.swap_memory())
# 输出结果：psutil.swap_memory() sswap(total=10600214528, used=3985588224, free=6614626304, percent=37.6, sin=0, sout=0)

r'''
    #注：返回的是字节为单位的整数，可以看到，总内存大小是8452730880 = 7.87 GB，已用3592646656 = 3.35 GB，使用了42.5%。
        而交换区大小是10600214528 = 9.87 GB。

'''