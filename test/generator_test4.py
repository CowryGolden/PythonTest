#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 生成器练习：自定义generator，充分理解函数的执行顺序和生成器的执行顺序；
'''
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

'''
    调用结果：
    >>> o = odd()
    >>> next(o)
    step 1
    1
    >>> next(o)
    step 2
    3
    >>> next(o)
    step 3
    5
    >>> next(o)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

    # 分析：可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。

    # 回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
    同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：
'''


'''
    #注：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator。
    特别注意：这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''