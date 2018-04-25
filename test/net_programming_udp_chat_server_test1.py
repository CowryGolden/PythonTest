#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 网络编程-UDP编程：UDP聊天服务器
    # 使用场景：
        UDP聊天服务器端

'''
# 
import socket, threading, time, re

user = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('192.168.1.70', 8888))
print('Bind UDP on 8888...')
while True:
    data, addr = s.recvfrom(1024)
    data = re.match(r'(\w+):([\s\w]*)', data.decode('utf-8')).groups()
    if len(data) ==2:
        if data[1] == 'online':
            user.append((data[0], addr))
            for n in user:
                s.sendto(b'%s online...' % data[0].encode('utf-8'), n[1])
            print('Received from %s:%s.' % addr)
            continue
    print('Received from %s:%s.' % addr)
    for n in user:
        if n[0] != data[0]:
            s.sendto(bytes('>>>' + data[0] + ':' + data[1], encoding='utf-8'), n[1])        




r'''
    #注：

'''