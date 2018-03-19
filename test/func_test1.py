#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Python函数可以返回多个值，但其实就是一个tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = move(100, 100, 60, math.pi / 6)
print('x,y =',x,y)
r = move(100, 100, 60, math.pi / 6)
print('r(tuple) =',r)