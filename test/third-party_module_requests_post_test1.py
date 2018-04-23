#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用第三方模块-requests：request的使用，POST方式
    # 使用场景：
        要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：        

'''
# 通过requests使用POST方式访问页面
import requests

r = requests.post('https://accounts.douban.com/login', data={'form_email' : 'abc@example.com', 'form_password' : '123456'})

print('r.status_code =', r.status_code)
print('r.encoding =', r.encoding)    # 自动检测网页编码
print('r.headers =', r.headers)    # 获取响应头
# print('r.text =', r.text)    # 获取网页文本内容
# print('r.content =', r.content)    # 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象

# requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
print('r.cookies =', r.cookies)
# print('r.cookies[\'ts\'] =', r.cookies['ts'])

# 要在请求中传入Cookie，只需准备一个dict传入cookies参数：
url = 'https://www.douban.com/'
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)
print('r.cookies =', r.cookies)
print('r.cookies[\'bid\'] =', r.cookies['bid'])

# 最后，要指定超时，传入以秒为单位的timeout参数：
url = 'https://github.io/'
r = requests.get(url, timeout=2.5) # 2.5秒后超时
print('r.status_code =', r.status_code)

r'''
    #注：requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
            params = {'key': 'value'}
            r = requests.post(url, json=params) # 内部自动序列化为JSON     
        类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
            >>> upload_files = {'file': open('report.xls', 'rb')}
            >>> r = requests.post(url, files=upload_files) 
        在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
        把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。      

'''