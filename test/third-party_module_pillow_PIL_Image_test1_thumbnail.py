#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用第三方模块-Pillow：PIL(Python Imaging Library)模块的Image模块使用
    # 使用场景：
        PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
        由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。
        安装Pillow
            如果安装了Anaconda，Pillow就已经可用了。否则，需要在命令行下通过pip安装：
                $ pip install pillow
            如果遇到Permission denied安装失败，请加上sudo重试。
        下面看一个例子看PIL是如何操作图像的       

'''
# 使用PIL中的Image进行图像缩放
from PIL import Image

# 打开一个jpg图像文件，注意是当前路径下的文件
im = Image.open('test.jpg')
# 获得图像尺寸
w, h = im.size    # 返回一个tuple
print('Original image size: %s * %s' % (w, h))
# 缩放到50%：
im.thumbnail((w/2, h/2))    # 注意这里出入参数为tuple，缩放后im.size的大小为缩放后的大小
print('Resize image to: %s * %s' % (im.size[0], im.size[1]))    # print('Resize image to: %s * %s' % (w/2, h/2))

# 把缩放后的图像用jpeg格式保存
im.save('test_thumbnail.jpg', 'jpeg')
print('Save the thumbnail is successful')
print('[Resize image, save after]: im.size =', im.size)

r'''
    #注：

'''