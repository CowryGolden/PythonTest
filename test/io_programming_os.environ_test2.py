#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-操作文件和目录：os模块的使用；os.environ的使用
    # 使用场景：
        如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
        如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
        我们来看看如何使用os模块的基本功能：
        在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
        要获取某个环境变量的值，可以调用os.environ.get('key')：
'''
# 要获取某个环境变量的值，可以调用os.environ.get('key')：

import os

print("os.environ.get('PATH') =", os.environ.get('PATH'))

# 若获取的属性不存在，则返回None，可以给以默认值以提示
print("os.environ.get('x', 'default') =", os.environ.get('x', 'default'))

r'''
    #注：执行结果
os.environ.get('PATH') = D:\ProgramFiles\Python364\Scripts\;D:\ProgramFiles\Python364\;D:\ProgramFiles\Java\jdk1.8.0_131\bin;D:\ProgramFiles\Java\jdk1.8.0_131\jre\bin;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;D:\ProgramFiles\mysql-5.7.16\bin;D:\Program Files\Git\cmd;D:\Program Files\VanDyke Software\Clients\;E:\MavenProject\plug-in\maven3.5.2\bin;D:\ProgramFiles\Anaconda3;D:\ProgramFiles\Anaconda3\Scripts;C:\Users\Golden Cowry\AppData\Local\GitHubDesktop\bin;C:\Program Files\Microsoft VS Code\bin

'''