#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 异步IO-asyncio模块：使用asyncio模块的异步IO
    # 使用场景：
        asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
        asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
        用asyncio实现Hello world代码如下：

'''
# 用asyncio实现异步打印Hello world
# 导入依赖
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world!')
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print('Hello again!')

# 获取Eventloop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()

r'''
    #注：代码解析：
        @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
        hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
        由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
        当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
        把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

'''