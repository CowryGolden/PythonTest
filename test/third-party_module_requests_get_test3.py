#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用第三方模块-requests：request的使用，返回类型为json
    # 使用场景：
        我们已经讲解了Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。
        更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。
        安装requests
            如果安装了Anaconda，requests就已经可用了。否则，需要在命令行下通过pip安装：
                $ pip install requests
            如果遇到Permission denied安装失败，请加上sudo重试。
        使用requests，要通过GET访问一个页面，只需要几行代码；
        对于带参数的URL，传入一个dict作为params参数；
        requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：    

'''
# requests请求返回类型为JSON，直接获取使用
import requests

r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
res = r.json()

print('r.json() =', r.json())
print("res['query']['results']['channel']['location']['city'] =", res['query']['results']['channel']['location']['city'])


r'''
    #注：

'''