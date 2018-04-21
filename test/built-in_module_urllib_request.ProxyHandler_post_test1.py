#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：urllib的request模块Post请求使用
    # 使用场景：
        如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：

'''
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
from urllib import request

proxy_handler = request.ProxyHandler({'http' : 'http://www.example.com:3128'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass

r'''
    #注：urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。
        伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。

'''