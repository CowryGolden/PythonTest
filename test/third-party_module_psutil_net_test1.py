#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用第三方模块-psutil：psutil模块获取网络信息
    # 使用场景：
        使用psutil模块的net_*相关方法获取网络接口和网络连接信息：

'''
# 使用psutil模块的net_*相关方法获取网络接口和网络连接信息：
import psutil

print('**** psutil.net_io_counters() =', psutil.net_io_counters())    # 获取网路读写字节/包的个数
# psutil.net_io_counters() = snetio(bytes_sent=175534569, bytes_recv=3125262944, packets_sent=1321366, packets_recv=6089974, errin=0, errout=0, dropin=0, dropout=0)

print('**** psutil.net_if_addrs() =', psutil.net_if_addrs())    # 获取网路结构信息

print('**** psutil.net_if_stats() =', psutil.net_if_stats())    # 获取网路接口状态

# 要获取当前网络连接信息时，使用net_connections()
print('**** psutil.net_connections() =', psutil.net_connections())
r"""  
使用psutil.net_connections()可能会有如下报错：
    >>> psutil.net_connections()
    Traceback (most recent call last):
    ...
    PermissionError: [Errno 1] Operation not permitted

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
    ...
    psutil.AccessDenied: psutil.AccessDenied (pid=3847)
你可能会得到一个AccessDenied错误，原因是psutil获取信息也是要走系统接口，而获取网络连接信息需要root权限，这种情况下，可以退出Python交互环境，用sudo重新启动：
    $ sudo python3
    Password: ******
    Python 3.6.3 ... on darwin
    Type "help", ... for more information.
    >>> import psutil
    >>> psutil.net_connections()  
"""


r'''
    #注：

'''