#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：xml模块使用SAX方式解析xml
    # 使用场景：
        XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用，所以，有必要了解如何操作XML。
        DOM vs SAX
        操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
        SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
        正常情况下，优先考虑SAX，因为DOM实在太占内存。
        在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。
        举个例子，当SAX解析器读到一个节点时：
            <a href="/">python</a>
        会产生3个事件：
            1、start_element事件，在读取<a href="/">时；
            2、char_data事件，在读取python时；
            3、end_element事件，在读取</a>时。
        用代码实验一下：        

'''
# 用SAX方式解析XML
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax : start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax : end_element: %s' % name)

    def char_data(self, text):
        print('sax : char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

r'''
    #注：需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。

'''