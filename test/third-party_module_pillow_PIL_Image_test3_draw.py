#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用第三方模块-Pillow：PIL(Python Imaging Library)模块的Image/ImageDraw/ImageFont/ImageFilter模块使用
    # 使用场景：
        PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：

'''
# 使用PIL中的Image/ImageDraw/ImageFont/ImageFilter模块生成验证码
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 生成随机字母
def rdmChar():
    # 随机计数器
    a = random.randint(1, 3)
    # 如果a==1返回大写字母
    if a == 1:
        return chr(random.randint(65, 90))
    elif a == 2:   # 如果a==2返回小写字母 
        return chr(random.randint(97, 122))
    else:    # 如果a==3返回数字 
        return chr(random.randint(48, 57))    


# 随机颜色1
def rdmColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))    

# 随机颜色2
def rdmColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))    

# 定义图片大小 240 * 60，并创建图片对象
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 36)    # 这里写相对路径系统找不到资源，或者使用：ImageFont.truetype('arial.ttf', 36) 
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rdmColor1())
# 输出文字 
for t in range(4):
    draw.text((60 * t + 10 + pow(-1,t)*random.randint(0, 10), 10 + pow(-1,t)*random.randint(0, 10)), rdmChar(), font=font, fill=rdmColor2())   # 第一个参数是位置参数，使用随机数使得位置浮动
    # image.rotate(random.randint(-30, 30), resample=Image.BILINEAR, expand=1)

# 模糊处理
image = image.filter(ImageFilter.BLUR)
image.save('test_code.jpg', 'jpeg')
image.show()    # 显示图像（打开图像文件）
print('Verification code generates successfully')        

r'''
    #注：如果运行的时候报错：
            IOError: cannot open resource 或者 OSError: cannot open resource
        这是因为PIL无法定位到字体文件的位置，可以根据操作系统提供绝对路径，比如：
            '/Library/Fonts/Arial.ttf' 或者 'C:\\Windows\\Fonts\\Arial.ttf'    

        要详细了解PIL的强大功能，请请参考Pillow官方文档：
            https://pillow.readthedocs.org/    

'''