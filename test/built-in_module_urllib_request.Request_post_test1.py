#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：urllib的request模块Post请求使用
    # 使用场景：
        如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
        我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：

'''
# 我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
from urllib import request, parse

print('Login to weibo.cn')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s : %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))    


r'''
    #注：如果登录成功，我们获得的响应如下：
            Status: 200 OK
            Server: nginx/1.2.0
            ...
            Set-Cookie: SSOLoginState=1432620126; path=/; domain=weibo.cn
            ...
            Data: {"retcode":20000000,"msg":"","data":{...,"uid":"1658384301"}} 
        如果登录失败，我们获得的响应如下：
            ...
            Data: {"retcode":50011015,"msg":"\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef","data":{"username":"zhoujincheng777@sian.com","errline":634}}       

'''