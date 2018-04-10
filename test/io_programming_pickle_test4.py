#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-序列化：对象序列化
    # 使用场景：
        我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
        序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
        反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
        Python提供了pickle模块来实现序列化。
        pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object；
        看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。
        当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
        也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
'''
# 直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
import pickle

# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
    

print('dump.txt中的bytes数据反序列化后的内容为 :', d)


r'''
    #注：变量的内容又回来了！
    当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
    Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
    
'''