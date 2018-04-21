#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：urllib的request模块Get请求练习
    # 使用场景：
        利用urllib读取JSON，然后将JSON解析为Python对象：

'''
# 利用urllib读取JSON，然后将JSON解析为Python对象：
from urllib import request
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        return json.loads(f.read().decode('utf-8'))  # 也可以为：json.load(f)；json.loads(s)把JSON的字符串反序列化为Python对象；json.load(fp)从file-like Object中读取字符串并反序列化为Python对象

# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')

r'''
    #注：

'''