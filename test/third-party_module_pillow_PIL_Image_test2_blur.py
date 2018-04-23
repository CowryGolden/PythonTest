#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用第三方模块-Pillow：PIL(Python Imaging Library)模块的Image、ImageFilter模块使用
    # 使用场景：
        PIL中其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
        比如，模糊效果也只需几行代码：

'''
# 使用PIL中的Image、ImageFilter进行图像模糊处理
from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径下文件
im = Image.open('test.jpg')
# 应用模糊滤镜
im1 = im.filter(ImageFilter.BLUR)
im1.save('test_blur.jpg', 'jpeg')
print('The image blur successfully')

r'''
    #注：

'''