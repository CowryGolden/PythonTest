#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 进程和线程-多线程：多线程中join的用法
    # 使用场景：
        首先需要明确几个概念：
        知识点一：
            当一个进程启动之后，会默认产生一个主线程，因为线程是程序执行流的最小单元，当设置多线程时，主线程会创建多个子线程，
            在python中，默认情况下（其实就是setDaemon(False)），主线程执行完自己的任务以后，就退出了，
            此时子线程会继续执行自己的任务，直到自己的任务结束，例子参见：process-thread_multithreading_join_test1.py。
        知识点二：
            当我们使用setDaemon(True)方法，设置子线程为守护线程时，主线程一旦执行结束，则全部线程全部被终止执行，
            可能出现的情况就是，子线程的任务还没有完全执行结束，就被迫停止，例子参见：process-thread_multithreading_join_test2.py。
        知识点三：
            此时join的作用就凸显出来了，join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，
            一直等待其他的子线程执行结束之后，主线程在终止，例子参见：process-thread_multithreading_join_test3.py。
        知识点四：
            join有一个timeout参数：
            1、当设置守护线程时，含义是主线程对于子线程等待timeout的时间将会杀死该子线程，最后退出程序。
                所以说，如果有10个子线程，全部的等待时间就是每个timeout的累加和。
                简单的来说，就是给每个子线程一个timeout的时间，让他去执行，时间一到，不管任务有没有完成，直接杀死。
            2、没有设置守护线程时，主线程将会等待timeout的累加和这样的一段时间，时间一到，主线程结束，
                但是并没有杀死子线程，子线程依然可以继续执行，直到子线程全部结束，程序退出。        

        【来源：https://www.cnblogs.com/cnkai/p/7504980.html】
'''
# Python多线程的默认情况（不设置守护线程，主线程结束，子线程继续执行）
import time, threading

def run():
    time.sleep(0.7)  # 设置的等待时间不能过长，否则在主线程结束后还未等到其执行，就观察不到其执行结果了
    print('当前线程的名字是 :', threading.current_thread().name)
    time.sleep(0.7)

if __name__ == '__main__':
    start_time = time.time()
    print('这是主线程 :', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    print('主线程结束了！', threading.current_thread().name)
    print('一共用时 :', time.time() - start_time)        


r'''
    #注：关键点：
        1、我们的计时是对主线程计时的，主线程结束，计时随之结束，打印出主线程的用时；
        2、主线程的任务完成之后，主线程随之结束，子线程继续执行自己的任务，直到全部的子线程的任务全部结束，至此程序才结束。

'''