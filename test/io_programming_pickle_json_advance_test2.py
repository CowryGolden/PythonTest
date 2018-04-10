#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # IO编程-序列化：JSON进阶，类对象的序列化
    # 使用场景：
        Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化；

'''
# 定义Student类，然后序列化：
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }

s = Student('Bob', 20, 88)
print('将Student类的对象转换为JSON字符串为 :', json.dumps(s, default=student2dict))

# 值得注意的是：下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
# print(json.dumps(s, default=lambda obj: obj.__dict__))，具体参见：io_programming_pickle_json_advance_test3.py

r'''
    #注：
        如果连class的实例对象都无法序列化为JSON，这肯定不合理！
        别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
        https://docs.python.org/3/library/json.html#json.dumps
        这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
        可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
        具体参见：io_programming_pickle_json_advance_test2.py
'''