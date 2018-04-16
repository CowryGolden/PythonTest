#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 进程和线程-多进程：Pool进程池的使用
    # 使用场景：
        Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
        普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
        因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
        子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
        所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

        如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
'''
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
import os, time, random
from multiprocessing import Pool

def long_time_task(name):
    print('Run task %s (%s) ...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')        
 

r'''
    #注：代码解读：
        对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
        请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
            p = Pool(5)
        就可以同时跑5个进程。    
        由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
'''