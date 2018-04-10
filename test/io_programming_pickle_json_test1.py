#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-序列化：JSON对象序列化和反序列化
    # 使用场景：
        如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
        因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
        JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
                -------------------------------------
                    JSON类型    Python类型
                    {}	        dict
                    []	        list
                    "string"	str
                    1234.56	    int或float
                    true/false	True/False
                    null	    None
                -------------------------------------
        Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：

'''
# 把Python对象变成一个JSON：
import json

d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d)  # dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

print('将Python的dict类型转换为JSON字符串为 :', json_str)

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
d = json.loads(json_str)  # dict对象；isinstance(d, dict) : True

print('将JSON字符串转换为Python的dict类型为 :', d)

r'''
    #注：由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。

'''