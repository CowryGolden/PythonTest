#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-操作文件和目录：os模块的使用；os.name的使用
    # 使用场景：
        如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
        如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
        我们来看看如何使用os模块的基本功能：
'''
# 使用os模块的os.name

import os

print('os.name :', os.name)


'''
    #注：如果是nt，就是Windows系统；如果是posix，说明系统是Linux、Unix或Mac OS X。

要获取详细的系统信息，可以调用uname()函数：
>>> os.uname()
posix.uname_result(sysname='Darwin', nodename='MichaelMacPro.local', release='14.3.0', version='Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64', machine='x86_64')

【特别注意：uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。】

'''