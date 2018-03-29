#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-定制类：__getitem__()的使用
    # 使用场景：
         list有个神奇的切片方法：
            >>> list(range(100))[5:10]
            [5, 6, 7, 8, 9]
        对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断，让oop_customized_class_getitem_test1.py中的Fib可以像list一样使用切片功能
'''
# __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断，让Fib可以像list一样使用切片功能
def getFibByIndex(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):    # n是索引
            return getFibByIndex(n)

        if isinstance(n, slice):    # n是切片
            start = n.start
            stop = n.stop
            step = n.step

            if start is None:
                start = 0
            if stop is None:
                raise ValueError('slice stop position can not be None')
            if step is None:
                step = 1

            L = []
            # 利用range的切片功能进行for循环
            for x in range(start, stop, step):
                L.append(getFibByIndex(x))
            return L

            # 如下写法没有判断step
            # a, b = 1, 1
            # L = []
            # for x in range(stop):
            #     if x >= start:
            #         L.append(a)
            #     a, b = b, a + b
            # return L        

# 现在试试Fib的切片：
f = Fib()
print('f[20] =', f[20])
print('f[0:5] =', f[0:5])
print('f[:10] =', f[:10])
print('f[:10:3] =', f[:10:3])
# print('f[::2] =', f[::2])  # stop位置参数为空时抛出异常
# 其中没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str

'''
    #注：与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
        总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

1 : 1
2 : 1
3 : 2
4 : 3
5 : 5
6 : 8
7 : 13
8 : 21
9 : 34
10 : 55
11 : 89
12 : 144
13 : 233
14 : 377
15 : 610
16 : 987
17 : 1597
18 : 2584
19 : 4181
20 : 6765
21 : 10946
22 : 17711
23 : 28657
24 : 46368
25 : 75025
    
'''