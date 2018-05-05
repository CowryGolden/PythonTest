#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 异步IO-asyncio模块：使用asyncio模块的异步IO
    # 使用场景：
        asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
        asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
        下面我们用Task封装两个coroutine观察异步IO的执行结果

'''
# 用Task封装两个coroutine观察异步IO的执行结果
# 导入依赖
import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1)
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

# 获取Eventloop
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

r'''
    #注：执行结果：
            Hello world! (<_MainThread(MainThread, started 7712)>)
            Hello world! (<_MainThread(MainThread, started 7712)>)
            (...暂停约1秒...)
            Hello again! (<_MainThread(MainThread, started 7712)>)
            Hello again! (<_MainThread(MainThread, started 7712)>)
        结果分析：
            由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
            如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。 

'''