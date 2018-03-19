#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 在Python中定义函数可以用必选参数、默认参数、可变参数、命名关键字参数和关键字参数，这5种参数可以组合使用。
    # 但是请注意：参数顺序必须是：
        【必选参数 -> 默认参数 -> 可变参数 -> 命名关键字参数  -> 关键字参数】      
'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2,c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

'''
    #注：通过上述一个tuple和dict调用函数，可知：
        对于任意函数，都可以通过类似 func(*args, **kw) 的形式调用它，无论它的参数是如何定义的
    ****特别注意****
    1）和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数；
        eg: def person(name, age, *, city, job):
                print(name, age, city, job)
            调用：person('Jack', 24, city='Beijing', job='Engineer')
            只接收city和job作为关键字参数。

    2）如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
        eg: def person(name, age, *args, city, job):
                print(name, age, args, city, job)
            调用：person('Jack', 24, city='Beijing', job='Engineer')
            注意：千万不能写成person('Jack', 24, 'Beijing', 'Engineer')调用，
            命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错；
            也就是说必须带上city和job关键字并赋值；

    3）虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
'''