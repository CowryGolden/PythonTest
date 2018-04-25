#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 网络编程-UDP编程：服务器
    # 使用场景：
        ## 服务器 ##
        TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。
        使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
        虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。
        我们来看看如何通过UDP协议传输数据。和TCP类似，使用UDP的通信双方也分为客户端和服务器。服务器首先需要绑定端口：

'''
# 编写一个简单的UDP服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。
import socket, threading, time

# 首先，创建一个基于IPv4和UDP协议的Socket：
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定IP和端口
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
# 创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：

# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
def udplink():
    while True:
        # 接收数据
        data, addr = s.recvfrom(1024)    # recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
        print('Received data from %s:%s.' % addr)    
        time.sleep(1)
        s.sendto(b'Hello, %s' % data, addr)

# 接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端连接：
while True:
    # 创建新线程来处理UDP连接：
    t = threading.Thread(target=udplink)
    t.start()



r'''
    #注：小结
        UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。

'''