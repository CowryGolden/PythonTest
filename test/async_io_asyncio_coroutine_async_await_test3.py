#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 异步IO-asyncio模块：使用async和await实现异步IO
    # 使用场景：
        自定义generator协程类型，并进行异步操作

'''
# 自定义generator协程类型，并进行异步操作
# 导入依赖
import asyncio

async def phase1():
    print('in phase1')
    return 'result1'

async def phase2(arg):
    print('in phase2')  
    return 'result2 derived from {}'.format(arg)  

async def outer():
    print('in outer')
    print('waiting for result1')
    result1 = await phase1()
    print('waiting for result2')
    result2 = await phase2(result1)
    return (result1, result2)  

loop  = asyncio.get_event_loop()
tasks = [outer()]
result_values = loop.run_until_complete(asyncio.wait(tasks))
print('result_values =', result_values)
loop.close()

r'''
    #注：

'''