#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-定制类：__getitem__()的使用
    # 使用场景：
        Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
            >>> Fib()[5]
            Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
            TypeError: 'Fib' object does not support indexing
        要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：    
'''
# 我们仍以斐波那契数列为例，写一个Fib类，可以表现得像list
class Fib(object):   
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

'''
# 错误写法：
class Fib(object):
    def __init__(self):
        self.__a, self.__b = 1, 1 # 初始化两个计数器a，b        
    def __getitem__(self, n):
        for x in range(n):
            self.__a, self.__b = self.__b, self.__a + self.__b
        return self.__a
此种写法中a,b为类变量，调用结束后，变量仍会在内存中保持，导致结果不正确（没有保持每次调用重新初始化变量）
'''
# 现在尝试把Fib实例用于for循环
f = Fib()
# print('f[0] =', f[0])
# print('f[1] =', f[1])
# print('f[5] =', f[5])
# print('f[10] =', f[10])
# print('f[15] =', f[15])
# print('f[20] =', f[20])
# print('f[25] =', f[25])
# print('f[100] =', f[100])
for x in range(30):
    print('f[%d] = %d' % (x, f[x]))

'''
    #注：

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