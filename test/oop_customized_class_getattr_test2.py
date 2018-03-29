#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-定制类：__getattr__()的使用
    # 使用场景：
        oop_customized_class_getattr_test1.py中的处理方式实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
        这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
        举个例子：
            现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
                http://api.server/user/friends
                http://api.server/user/timeline/list
            如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
            利用完全动态的__getattr__，我们可以写出一个链式调用： 
'''
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):
    def __init__(self, path = ''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path

    __repr__ = __str__ 

    __call__ = __getattr__  # 此句可以将Chain().users('michael').repos转为/users/michael/repos

# 测试
print('Chain().status.user.timeline.list :', Chain().status.user.timeline.list)

# 还有些REST API会把参数放到URL中，比如GitHub的API：
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
print("Chain().users('michael').repos =", Chain().users('michael').repos)
# 就可以非常方便地调用API了。有兴趣的童鞋可以试试写出来。(遗留作业：在类中加入：__call__ = __getattr__即可)
'''
对上面写法的简单解释：
可以简单地理解成 . 和 (...) 都是一种运算符号。
比如 + 运算就相当于调用 __add__ 一样，
. 就相当于调用 __getattr__，
(...) 就相当于调用 __call__。
于是 users michael repos 就被这些运算符号给连起来了。
'''

'''
    #注：这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
    
'''