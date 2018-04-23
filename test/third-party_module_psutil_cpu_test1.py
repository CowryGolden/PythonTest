#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用第三方模块-psutil：psutil模块获取cpu信息
    # 使用场景：
        用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，
        如ps，top，free等等。要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。
        在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，
        它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
        安装psutil
            如果安装了Anaconda，psutil就已经可用了。否则，需要在命令行下通过pip安装：
                $ pip install psutil
            如果遇到Permission denied安装失败，请加上sudo重试。
        获取CPU信息
            通过psutil模块的cup_*相关方法获取cpu信息，具体查看如下例子：        

'''
# 使用psutil模块的cup_*相关方法获取cpu信息
import psutil
# 获取CPU的信息：
print('psutil.cpu_count() =', psutil.cpu_count())    # 获取cpu逻辑数量

print('psutil.cpu_count(logical=False) =', psutil.cpu_count(logical=False))    # 获取cpu物理个数，4说明是4核超线程，8则是8核非超线程

# 统计CPU的用户/系统/空闲时间
print('psutil.cpu_times() =', psutil.cpu_times())

# 再实现类似top命令的CPU使用率，每秒刷新1次，累计10次：
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

r'''
    #注：

'''