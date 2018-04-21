#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：html模块HTMLParser练习
    # 使用场景：
        找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

'''
# 使用HTMLParser解析HTML
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)   # 继承于HTMLParser类，所以初始化的时候需要有这一句
        self.flag = 0               # 是否为要获取的标签标志
        self.res = []               # 返回的结果集
        self.is_get_data = None     # 要获取的数据内容标识key：title、time、addr等

    def handle_starttag(self, tag, attrs):
        # print('<%s>' % tag)
        # 查看网页源码，找到包裹事件的元素
        if tag == 'ul':
            for attr in attrs:
                if re.match(r'list-recent-events', attr[1]):
                    self.flag = 1

        # 处理包裹时间名称的a元素
        if tag == 'a' and self.flag == 1:
            self.is_get_data = 'title'

        # 处理包裹事件时间的time元素
        if tag == 'time' and self.flag == 1:
            self.is_get_data = 'time'

        # 处理包裹事件地点的span元素
        if tag == 'span' and self.flag == 1:
            self.is_get_data = 'addr'
            # for attr in attrs:
            #     if re.match(r'event-location', attr[1]):    # 需要过滤出存地址的span；因为在ul下面有两个span标签，一个存隐藏的时间，一个存地址
            #         self.is_get_data = 'addr'                    

    def handle_endtag(self, tag):
        # print('</%s>' % tag)
        if self.flag == 1 and tag == 'ul':
            self.flag = 0

    def handle_startendtag(self, tag, attrs):
        # print('<%s/>' % tag)
        pass

    def handle_data(self, data):
        # print('data :', data)
        if self.is_get_data and self.flag == 1:
            if self.is_get_data == 'title':
                self.res.append({self.is_get_data : data})
            else:
                self.res[len(self.res) - 1][self.is_get_data] = data
            self.is_get_data = None    
            """ 
                关于以上代码的解释：
                    res是一个list，存储所有会议
                    list的元素是dict
                    每个dict表示一个会议

                    获得title,即会议名时，给res添加一个新dict：
                    self.res.append({self.is_get_data: data})
                    res 由[] 变为 [{'title':'PyCascades 2018'}]

                    获得addr，time这样的其它属性时,先把最后一个dict（即当前处理的dict）取出：
                    即self.res[len(self.res) - 1]
                    再把新属性加入：
                    self.res[len(self.res) - 1][self.is_get_data] = data
                    [{'title':'PyCascades 2018','time':'22 Jan. – 24 Jan.'}]
            """

    def handle_comment(self, data):
        # print('<!--', data, '-->')
        pass

    def handle_entityref(self, name):
        # print('&%s;' % name)  
        pass

    def handle_charref(self, name):
        # print('&#%s;' % name)
        pass

parser = MyHTMLParser()

with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')

parser.feed(data)
for item in parser.res:
    print('------------------------')
    for k, v in item.items():
        print('%s : %s' % (k, v))

r'''
    #注：feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
        特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。
        利用HTMLParser，可以把网页中的文本、图像等解析出来。

'''