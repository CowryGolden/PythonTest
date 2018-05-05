#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 异步IO-asyncio模块：使用async和await实现异步IO
    # 使用场景：
        用asyncio的异步网络连接来获取sina、sohu和163的网站首页；
        使用Python从3.5版本开始为asyncio提供了async和await的新语法重写async_io_asyncio_coroutine_test3.py
        异步获取sina、sohu和163的网站首页源码并运行；
        为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
        只需要做两步简单的替换：
            1、把@asyncio.coroutine替换为async；
            2、把yield from替换为await。

'''
# 用Python3.5后提供的新语法async和await实现异步网络连接来获取sina、sohu和163的网站首页：
# 导入依赖
import asyncio

async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))    
    # Ignore the body, close the socket
    writer.close()

# 获取Eventloop
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

r'''
    #注：可见3个连接由一个线程通过coroutine并发完成。
        注意：在HTTP响应的头部：
            1、每个Header一行一个，换行符是\r\n。
            2、当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。
            3、HTTP响应如果包含body，通过\r\n\r\n来分隔。请再次注意，Body的数据类型由Content-Type头来确定，如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。
            4、当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，所以，看到Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据。压缩的目的在于减少Body的大小，加快网络传输。

        总结：
            1、asyncio提供了完善的异步IO支持；
            2、异步操作需要在coroutine中通过yield from完成；
            3、多个coroutine可以封装成一组Task然后并发执行。

'''