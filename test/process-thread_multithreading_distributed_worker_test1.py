#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 进程和线程-分布式进程：worker任务进程【运行的时候最好用cmd终端】
    # 使用场景：
        在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
        Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
        一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
        举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，
            希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
        原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
        我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务；
        然后，在另一台机器上启动任务进程（本机上启动也可以）。       

'''
# 将任务分布到两台机器上（一台机器上也可以），实现简单的分布式
import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字：
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行***_master_***.py的机器：
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码保持与master中设置的完全一致：
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接：
try:
    m.connect()
except:
    print('请先启动task master')
    # sys.exit('Sorry,goodbay!')    
# 获取Queue的对象：
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务，并把结果写入result队列：
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('Run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('Task queue is empty.')
# 处理结束：
print('Worker exit.')                



r'''
    #注：任务进程要通过网络连接到服务进程，所以要指定服务进程的IP。
        现在，可以试试分布式进程的工作效果了。先启动***_master_***.py服务进程：
        -------------------------------------------------------------------------------------
        这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布到几台甚至几十台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。
        Queue对象存储在哪？注意到task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中：

                                                     │
        ┌─────────────────────────────────────────┐  │  ┌──────────────────────────────────────┐
        │task_master.py                           │  │  │task_worker.py                        │
        │                                         │  │  │                                      │
        │  task = manager.get_task_queue()        │  │  │  task = manager.get_task_queue()     │
        │  result = manager.get_result_queue()    │  │  │  result = manager.get_result_queue() │
        │              │                          │  │  │              │                       │
        │              │                          │  │  │              │                       │
        │              ▼                          │  │  │              │                       │
        │  ┌─────────────────────────────────┐    │  │  │              │                       │
        │  │QueueManager                     │    │  │  │              │                       │
        │  │ ┌────────────┐ ┌──────────────┐ │    │  │  │              │                       │
        │  │ │ task_queue │ │ result_queue │ │<───┼──┼──┼──────────────┘                       │
        │  │ └────────────┘ └──────────────┘ │    │  │  │                                      │
        │  └─────────────────────────────────┘    │  │  │                                      │
        └─────────────────────────────────────────┘  │  └──────────────────────────────────────┘
                                                     │
                                                  Network
        而Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。
        authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果task_worker.py的authkey和task_master.py的authkey不一致，肯定连接不上。
        -------------------------------------------------------------------------------------
        小结：
            1、Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
            2、注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。
        -------------------------------------------------------------------------------------

        【代码解析：https://blog.csdn.net/lilong117194/article/details/76051843
            https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431929340191970154d52b9d484b88a7b343708fcc60000#0
        】

'''