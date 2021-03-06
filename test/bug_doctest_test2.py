#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 错误、调试和测试-文档调试：文档测试（doctest）
    # 使用场景：
        如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码。比如re模块就带了很多示例代码，可以把这些示例代码在Python的交互式环境下输入并执行，结果与文档中的示例代码显示的一致。                     
        并且，Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
        doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。
'''
# 让我们用doctest来测试上次编写的Dict类：

class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)    

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()        

'''
    #注：


'''