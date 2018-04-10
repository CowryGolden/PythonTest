#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-StringIO和BytesIO：StringIO（读写方法使用）
    # 使用场景：
        很多时候，数据读写不一定是文件，也可以在内存中读写。
        StringIO顾名思义就是在内存中读写str。
        要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
'''
# 创建StringIO并进行读写操作：
from io import StringIO
# 创建StringIO
f = StringIO()
# write()方法返回所写字符串的长度
print("f.write('Hello') =", f.write('Hello'))
print("f.write(' ') =", f.write(' '))
print("f.write('World') =", f.write('World!'))
# getvalue()方法用于获得写入后的字符串
print('f.getvalue() =', f.getvalue())

'''
    #注：


'''