#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：struct模块应用，Windows位图.bmp文件二进制编码分析
    # 使用场景：
        Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下。
        首先找一个bmp文件，没有的话用“画图”画一个。
        读入前30个字节来分析：
            s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

'''
# 利用struct模块分析Windows的.bmp位图二进制码
import struct

with open('E:/PythonWorkspace/test/test_bmp.bmp', 'rb') as f:
    # print(f.read())
    fb_data = f.read()    # 读取二进制字符串
# 截取二进制    
# fb_data_30 = fb_data[:30]
# print('fb_data_30 =', fb_data_30)  # fb_data_30 = b'BM6\x8c\n\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\x80\x02\x00\x00h\x01\x00\x00\x01\x00\x18\x00'
info = struct.unpack('<ccIIIIIIHH', fb_data[:30])
print('info =', info)    # info = (b'B', b'M', 691254, 0, 54, 40, 640, 360, 1, 24)

r'''
    #注：BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
            两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
            一个4字节整数：表示位图大小；
            一个4字节整数：保留位，始终为0；
            一个4字节整数：实际图像的偏移量；
            一个4字节整数：Header的字节数；
            一个4字节整数：图像宽度；
            一个4字节整数：图像高度；
            一个2字节整数：始终为1；
            一个2字节整数：颜色数。
        所以，组合起来用unpack读取：info = (b'B', b'M', 691254, 0, 54, 40, 640, 360, 1, 24)
        结果显示，b'B'、b'M'说明是Windows位图，文件大小为691254字节，位图大小为640x360，颜色数为24。    

'''