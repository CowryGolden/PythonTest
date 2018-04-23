#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用第三方模块-psutil：psutil模块获取进程信息
    # 使用场景：
        使用psutil模块的pids()、Porcess()等方法获取进程信息：

'''
# 使用psutil模块的pids()、Porcess()等方法获取进程信息：
import psutil

print('psutil.pids() =', psutil.pids())    # 或有所有进程ID

p = psutil.Process(14752)    # 获取指定进程ID=15648，其实就是当前Python交互环境
print('p.name() =', p.name())    # 获取进程名称
print('p.exe() =', p.exe())    # 获取进程exe路径
print('p.cwd() =', p.cwd())    # 获取进程工作目录
print('p.cmdline() =', p.cmdline())    # 获取进程启动的命令行
print('p.ppid() =', p.ppid())    # 获取父进程ID
print('p.parent() =', p.parent())    # 获取父进程
print('p.children() =', p.children())    # 获取子进程列表
print('p.status() =', p.status())    # 获取进程状态
print('p.username() =', p.username())    # 获取进程用户名
print('p.create_time() =', p.create_time())    # 获取进程创建时间
# print('p.terminal() =', p.terminal())    # 获取进程终端  # AttributeError: 'Process' object has no attribute 'terminal'
print('p.cpu_times() =', p.cpu_times())    # 获取进程使用的CPU时间
print('p.memory_info() =', p.memory_info())    # 获取进程使用的内存
print('p.open_files() =', p.open_files())    # 获取进程远程打开的文件列表
print('p.connections() =', p.connections())    # 获取进程相关网络连接列表
print('p.num_threads() =', p.num_threads())    # 获取进程的线程数量
print('p.threads() =', p.threads())    # 获取进程的所有线程信息
print('p.environ() =', p.environ())    # 获取进程的环境变量信息
# print('p.terminate() =', p.terminate())    # 结束进程    # 自己把自己结束了

# psutil还提供了一个test()函数，可以模拟出ps命令的效果：
print('--------------------psutil.test()-----------------------')
print(psutil.test())

r'''
    #注：获取网络连接类似，获取一个root用户的进程需要root权限，启动Python交互环境或者.py文件时，需要sudo权限。
        psutil使得Python程序获取系统信息变得易如反掌。
        psutil还可以获取用户信息、Windows服务等很多有用的系统信息，具体请参考psutil的官网：https://github.com/giampaolo/psutil

'''