#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 进程和线程-多进程：子进程
    # 使用场景：
        很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
        subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
        下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
'''
# 如果子进程还需要输入，则可以通过communicate()方法输入：      
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))    # windows系统默认为gbk不能使用utf-8
print('Exit code:', p.returncode)

r'''
    #注：上面的代码相当于在命令行执行命令nslookup，然后手动输入：
            set q=mx
            python.org
            exit
    
'''