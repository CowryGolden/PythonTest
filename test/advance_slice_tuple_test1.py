#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 练习：list或tuple的切片操作，字符串'xxx'也可以看成一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串。
'''
T = (0,1,2,3,4,5)
S = 'ABCDEFGH'

print('T =', T)
print('S =', S)

print('T[:3] =', T[:3]) # tuple也是一种list，其tuple是不变的，其切片操作结果仍为tuple
print('S[::2] =', S[::2])

'''
    #注：
'''