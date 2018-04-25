#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 网络编程-UDP编程：UDP聊天客户端
    # 使用场景：
        UDP聊天客户端

'''
# 
import socket, threading, time, re

def updlink(sock, addr):
    while True:
        time.sleep(0.1)
        print(sock.recv(1024).decode('utf-8'))

print('input your server ip:')
while True:
    ip = input()
    if re.match(r'\d{1,3}[.\d{1,3}]{3}', ip):
        break
    print('invaild IP')

print('input your name:')  
name = input()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(bytes(name + ':' + 'online', encoding='utf-8'), (ip, 8888))
t = threading.Thread(target=updlink, args=(s, (ip, 8888)))
t.start()
while True:
    data = input()
    s.sendto(bytes(name + ':' + data, encoding='utf-8'), (ip, 8888))
s.close()




r'''
    #注：

'''