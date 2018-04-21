#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：xml模块，构建简单的xml
    # 使用场景：
        除了解析XML外，如何生成XML呢？99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串：

'''
# 使用拼接字符串方式生成XML
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append('some & data')    # L.append(encode('some & data'))
L.append(r'</root>')
print(''.join(L))

r'''
    #注：如果要生成复杂的XML呢？建议你不要用XML，改成JSON。
        解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据。

'''