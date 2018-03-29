#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程：使用 @property 练习
    # 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：    
'''
class Screen(object):
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be integer!')
        if value < 0:
            raise ValueError('width must more than zero!')    
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be integer!')
        if value < 0:
            raise ValueError('height must more than zero!') 
        self.__height = value

    # 定义只读属性resolution
    @property
    def resolution(self):
        return self.__width * self.__height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

'''
    #注：
   
'''