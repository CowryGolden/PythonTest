#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # IO编程-序列化：JSON进阶，类对象的反序列化
    # 使用场景：
        Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化；
        同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
'''
# 将JSON对象(dict类型实例)反序列化为类对象
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)    

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"name": "Bob", "age": 20, "score": 88}'

print('将JSON对象转为Student类实例对象 :', json.loads(json_str, object_hook=dict2student))

s = json.loads(json_str, object_hook=dict2student)
print(s)
# print('s.age =', s.age)
# print('s.score =', s.score)

r'''
    #注：序列化小结：
            1、Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
            2、json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。
              但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。

'''