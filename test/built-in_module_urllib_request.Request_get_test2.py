#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：urllib的request模块模拟Get请求
    # 使用场景：
        如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：

'''
# 模拟浏览器发送GET请求，模拟iPhone 6去请求豆瓣首页：
from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s : %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))    

r'''
    #注：这样豆瓣会返回适合iPhone的移动版网页：
        ...
            <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
            <meta name="format-detection" content="telephone=no">
            <link rel="apple-touch-icon" sizes="57x57" href="http://img4.douban.com/pics/cardkit/launcher/57.png" />
        ...    

'''