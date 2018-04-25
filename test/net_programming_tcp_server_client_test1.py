#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 网络编程-TCP编程：服务器
    # 使用场景：
        ## 服务器 ##
        和客户端编程相比，服务器编程就要复杂一些。
        服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。
        所以，服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接。由于服务器会有大量来自客户端的连接，
        所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。
        但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。
        我们来编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。

'''
# 编写一个简单的TCP服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。
import socket, threading, time

# # 如下注释内容为服务器端代码，需要放在服务器端文件中单独运行：net_programming_tcp_server_server_test1.py
# # 首先，创建一个基于IPv4和TCP协议的Socket：
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # 然后，我们要绑定监听的地址和端口。服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可以用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址。127.0.0.1是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，也就是说，外部的计算机无法连接进来。
# # 端口号需要预先指定。因为我们写的这个服务不是标准服务，所以用9999这个端口号。请注意，小于1024的端口号必须要有管理员权限才能绑定：
# # 绑定IP与监听端口
# s.bind(('127.0.0.1', 9999))

# # 紧接着，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
# s.listen(5)
# print('Waiting for connection...')

# # 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
# def tcplink(sock, addr):    # 此方法一定要定义在threading.Thread(target=tcplink, args=(sock, addr))之前，否则报错：NameError: name 'tcplink' is not defined
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8')  == 'exit':
#             break
#         sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))  
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)

# # 接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端连接：
# while True:
#     # 接受一个新连接
#     sock, addr = s.accept() # Wait for an incoming connection. Return a new socket representing the connection, and the address of the client. For IP sockets, the address info is a pair (hostaddr, port).
#     # 创建新线程来处理TCP连接：
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()

# # 连接建立后，服务器首先发一条欢迎信息，然后等待客户端数据，并加上Hello再发送给客户端。如果客户端发送了exit字符串，就直接关闭连接。

# 如下内容要放到客户端文件中单独运行：net_programming_tcp_server_client_test1.py
# 要测试这个服务器程序，我们还要编写一个客户端程序：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 9999))
# 接收欢迎信息
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit') 
s.close()   

# 我们需要打开两个命令行窗口，一个运行服务器程序，另一个运行客户端程序，就可以看到效果了。
# 需要注意的是，客户端程序运行完毕就退出了，而服务器程序会永远运行下去，必须按Ctrl+C退出程序。

r'''
    #注：小结
        用TCP协议进行Socket编程在Python中十分简单，对于客户端，要主动连接服务器的IP和指定端口，对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。
        同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。

'''