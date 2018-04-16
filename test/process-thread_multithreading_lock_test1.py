#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 进程和线程-多线程：Lock引入先导（为什么要使用Lock：来看看多个线程同时操作一个变量怎么把内容给改乱了：）
    # 使用场景：
        多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
        而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
        因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

'''
# 来看看多个线程同时操作一个变量怎么把内容给改乱了：
import time, threading

# 假定这是你的银行存款
balance = 0

def change_it(n):
    # 先存后取，结果应该为0：
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))        
t1.start()
t2.start()
t1.join()
t2.join()
print('balance =', balance)


r'''
    #注：结果分析：
        我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，
        但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
        原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
            balance = balance + n
        也分两步：
            1、计算balance + n，存入临时变量中；
            2、将临时变量的值赋给balance。
        也就是可以看成：
            x = balance + n
            balance = x
        由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：
        -------------------------------------------------------------   
            初始值 balance = 0

            t1: x1 = balance + 5 # x1 = 0 + 5 = 5
            t1: balance = x1     # balance = 5
            t1: x1 = balance - 5 # x1 = 5 - 5 = 0
            t1: balance = x1     # balance = 0

            t2: x2 = balance + 8 # x2 = 0 + 8 = 8
            t2: balance = x2     # balance = 8
            t2: x2 = balance - 8 # x2 = 8 - 8 = 0
            t2: balance = x2     # balance = 0

            结果 balance = 0
        -------------------------------------------------------------
        但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：
        -------------------------------------------------------------
            初始值 balance = 0

            t1: x1 = balance + 5  # x1 = 0 + 5 = 5

            t2: x2 = balance + 8  # x2 = 0 + 8 = 8
            t2: balance = x2      # balance = 8

            t1: balance = x1      # balance = 5
            t1: x1 = balance - 5  # x1 = 5 - 5 = 0
            t1: balance = x1      # balance = 0

            t2: x2 = balance - 8  # x2 = 0 - 8 = -8
            t2: balance = x2   # balance = -8

            结果 balance = -8
        -------------------------------------------------------------
        究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。
        两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成了负数，所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。
        如果我们要确保balance计算正确，就要给change_it()上一把锁，具体参加：process-thread_multithreading_lock_test2.py

'''