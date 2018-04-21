#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：struct模块应用，检查任意文件是否是位图
    # 使用场景：
        请编写一个函数，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。

'''
# 利用struct模块分析文件是否是位图
import base64, struct

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info(data):
    info = struct.unpack('<ccIIIIIIHH', data[:30])    # ccIIIIIIHH也可以写作2c6I2H（2*1+6*4+2*2=30），注意因为前面的解析格式只有30位，所以后面的byte串只取前30位，否则会出错
    # print('info =', info)    # info = (b'B', b'M', 616, 0, 54, 40, 28, 10, 1, 16)
    # print(data[:2] == b'BM')
    if info[0] == b'B' and (info[1] == b'M' or info[1] == b'A'):
        return {
            'width': info[6],
            'height': info[7],
            'color': info[9]
        }
    else:
        raise TypeError('This file is not a bmp')    

# 测试
bi = bmp_info(bmp_data)

print('width =', bi['width'])
print('height =', bi['height'])
print('color =', bi['color'])

assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

r'''
    #注：BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
            前两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
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