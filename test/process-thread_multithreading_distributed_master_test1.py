#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 进程和线程-分布式进程：master服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：【运行的时候最好用cmd终端】
    # 使用场景：
        在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
        Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
        一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
        举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，
            希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
        原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
        我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：        

'''
# 将任务分布到两台机器上，实现简单的分布式
import time, random, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support    # 引入freeze_support，否则报错：RuntimeError:The "freeze_support()" line can be omitted if the program is not going to be frozen to produce an executable.

# 发送任务的队列：
task_queue = queue.Queue()
# 接收结果的队列：
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

''' Windows运行的代码
# Windows下不支持匿名函数，所以将返回发送任务队列（return task_queue）和接收结果队列（return result_queue）的函数提取出来定义即可
# 我们给return_task_queue的网络调用接口取了一个别名get_task_queue,而return_result_queue的别名是get_result_queue，方便区分对哪个queue进行操作。
''' 
# 定义返回发送任务队列函数
def return_task_queue():
    global task_queue
    return task_queue
# 定义返回接收结果队列函数
def return_result_queue():
    global result_queue
    return result_queue

def test():
    # 把两个Queue都注册到网络上，callable参数关联了Queue对象：(以下为Windows下运行的代码)    
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 把两个Queue都注册到网络上，callable参数关联了Queue对象：(以下为Unix/Linux下运行的代码)
    '''Unix/Linux下运行代码：
    # 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
    # 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
    # 其中task_queue和result_queue是两个队列，分别存放任务和结果。它们用来进行进程间通信，交换对象。
    QueueManager.register('get_task_queue', callable=lambda: task_queue)  # Windows下不支持匿名函数，所以将其提取出来定义即可
    QueueManager.register('get_result_queue', callable=lambda: result_queue)  # Windows下不支持匿名函数，所以将其提取出来定义即可
    # Windows报错：_pickle.PicklingError: Can't pickle <function <lambda> at 0x0000001C93D846A8>: attribute lookup <lambda> on __main__ failed
    '''
    # 绑定端口5000，设置验证码'abc'：(Linux下可以写IP也可以不写)
    # manager = QueueManager(address=('', 5000), authkey=b'abc')
    # windows必须写ip地址
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()
    # 获得通过网络访问的Queue对象：
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去：
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果：
    print('Try get results...') 
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except queue.Empty:
            print('Result queue is empty.')    
    # 关闭：
    manager.shutdown()
    print('Master exit.')       

if __name__ == '__main__':
    freeze_support()
    print('Master start...')
    test()

r'''
    #注：请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
        但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，
        那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。
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