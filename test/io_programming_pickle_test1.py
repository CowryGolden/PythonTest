#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-序列化：对象序列化
    # 使用场景：
        我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
        序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
        反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
        Python提供了pickle模块来实现序列化。
'''
# 首先，我们尝试把一个对象序列化并写入文件：
import pickle

d = dict(name='Bob', age=20, score=88)

pb = pickle.dumps(d)

print('the bytes of dict :', pb)


r'''
    #注：pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：

'''