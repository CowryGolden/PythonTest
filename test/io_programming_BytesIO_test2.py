#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-StringIO和BytesIO：BytesIO（读取二进制）
    # 使用场景：
        StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
        BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes；
        和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取；

'''
# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
from io import BytesIO
# 创建并初始化BytesIO
# 错误写法 f = BytesIO("b'\xe4\xb8\xad\xe6\x96\x87'")  # 请注意，写入的不是str，而是经过UTF-8编码的bytes。此种写法会报错：TypeError: a bytes-like object is required, not 'str'
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# 像对文件一样读取
print('f.read() =', f.read())

'''
    #注：请注意，写入的不是str，而是经过UTF-8编码的bytes。


'''