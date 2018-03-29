#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-偏函数练习：自己实现一个 partial 偏函数

'''
class partial:
    def __new__(cls, func, *args, **kwargs):
        if not callable(func):
            raise TypeError("the first argument must be callable")
        self = super().__new__(cls)

        self.func = func
        self.args = args
        self.kwargs = kwargs
        return self
    
    def __call__(self, *args, **kwargs):
        newkeywords = self.kwargs.copy()
        newkeywords.update(kwargs)
        return self.func(*self.args, *args, **newkeywords)

# 测试

def add(x, y):
    return x + y

inc = partial(add, y = 1)
print(inc(41))  # 42

'''
    #注：
'''