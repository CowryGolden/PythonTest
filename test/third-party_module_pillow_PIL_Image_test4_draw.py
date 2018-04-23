#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用第三方模块-Pillow：PIL(Python Imaging Library)模块的Image/ImageDraw/ImageFont/ImageFilter模块使用
    # 使用场景：
        PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
        增加功能：生成的字符带旋转角度

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

def randPoint(width, height):
    return (random.randint(0, width),random.randint(0, height))

# 定义图片大小 240 * 60，并创建图片对象
width = 60 * 4
height = 60
color = (255, 255, 255)    # 设置图片背景颜色
image = Image.new('RGB', (width, height), color)    # 创建底图（背景图）
# 创建Font对象，设置字体样式及大小
font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 36)    # 这里写相对路径系统找不到资源，或者使用：ImageFont.truetype('arial.ttf', 36) 

# 创建大的背景Draw对象
draw = ImageDraw.Draw(image)
# # 填充每个像素
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rdmColor1())

# 输出文字（要想生成的字符带旋转，得为每个字符生成单个图片，旋转后，再粘贴到原来的大图片中） 
for t in range(4):
    fw, fh = 40, 40  # 定义字符图片的大小
    im_font = Image.new('RGBA', (fw, fh), color)
    dw_font = ImageDraw.Draw(im_font)
    dw_font.text((2, 0), rdmChar(), font=font, fill=rdmColor2())   # 第一个参数是位置参数，使用随机数使得位置浮动
    im_font = im_font.rotate(random.randint(-45, 45), resample=Image.BILINEAR, expand=1)
    im_font_back = Image.new('RGBA', im_font.size, color)    # 创建单个字符的背景颜色
    im_font = Image.alpha_composite(im_font_back, im_font)    # 改变底色    
    image.paste(im_font, (60*t + 10, random.randint(0,10)))   # 将单个字符图片粘到大的背景图上


# 生成20条随机干扰线
for i in range(20):
    draw.line([randPoint(240, 60), randPoint(240, 60)], fill=rdmColor1())
    # del draw

# 模糊处理
# image = image.filter(ImageFilter.BLUR)
image.save('test_rotate_code.jpg', 'jpeg')
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