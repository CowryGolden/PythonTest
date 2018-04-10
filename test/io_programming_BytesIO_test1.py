#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-StringIO和BytesIO：BytesIO（读写方法使用）
    # 使用场景：
        StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
        BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：

'''
# 创建BytesIO并进行读写操作：
from io import BytesIO
# 创建BytesIO
f = BytesIO()
# 使用write()方法进行二进制数据写操作(一个中文utf-8编码占3个字节)
print("f.write('中文'.encode('utf-8')) =", f.write('中文'.encode('utf-8')))
# getvalue()方法用于获得写入后的字符串
print(f.getvalue())

'''
    #注：请注意，写入的不是str，而是经过UTF-8编码的bytes。


'''