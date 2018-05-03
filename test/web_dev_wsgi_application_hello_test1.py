#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # Web开发-WSGI接口：WSGI处理函数
    # 使用场景：
        正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。
        这个接口就是WSGI：Web Server Gateway Interface。
        WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”：
            def application(environ, start_response):
                start_response('200 OK', [('Content-Type', 'text/html')])
                return [b'<h1>Hello, web!</h1>']    
        上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
            1、environ：一个包含所有HTTP请求信息的dict对象；
            2、start_response：一个发送HTTP响应的函数。   
        在application()函数中，调用：
            start_response('200 OK', [('Content-Type', 'text/html')])
        就发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。
        通常情况下，都应该把Content-Type头发送给浏览器。其他很多常用的HTTP Header也应该发送。
        然后，函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器。
        有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，通过start_response()发送Header，最后返回Body。
        整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，我们只负责在更高层次上考虑如何响应请求就可以了。
        不过，等等，这个application()函数怎么调用？如果我们自己调用，两个参数environ和start_response我们没法提供，返回的bytes也没法发给浏览器。
        所以application()函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，我们可以挑选一个来用。但是现在，我们只想尽快测试一下我们编写的application()函数真的可以把HTML输出到浏览器，所以，要赶紧找一个最简单的WSGI服务器，把我们的Web应用程序跑起来。
        好消息是Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。             

'''
# 我们先编写*_hello*.py，实现Web应用程序的WSGI处理函数：

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO'].encode('iso-8859-1').decode('utf-8')[1:]
    # print('path =', path)
    body = '<h1>Hello, %s!</h1>' % (path or 'web')    # 解决输入中文乱码问题，不可以输中文： (environ['PATH_INFO'][1:] or 'web')
    # print('body =', body)
    return [body.encode('utf-8')]    # 中文换为：[body.encode('gbk')]
    # return [b'<h1>Hello, Web!</h1>']

r'''
    #注：然后，再编写一个*_server*.py，负责启动WSGI服务器，加载application()函数；
        如果你觉得这个Web应用太简单了，可以稍微改造一下，从environ里读取PATH_INFO，这样可以显示更加动态的内容：
            # *_hello*.py可以做如下改造
            def application(environ, start_response):
                start_response('200 OK', [('Content-Type', 'text/html')])
                body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
                return [body.encode('utf-8')]

'''