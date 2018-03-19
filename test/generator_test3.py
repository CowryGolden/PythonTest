#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 生成器练习：使用generator实现斐波那契数列(Fibonacci)；generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
    eg：1,1,2,3,5,8,13,21,34,...
    分析：斐波那契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：下面将行数变成generator，只需要把print(b)改为yield b就可以了：
'''
def fib(max): # max表示最大生成斐波那契数列个数
    n, a, b = 0, 0, 1
    while n < max:
        yield b # yield b为generator写法，print(b)为函数写法
        a, b = b, a + b # 相当于 t=(b, a+b); a = t[0]; b = t[1];
        n = n + 1
    return 'done'
'''
    # 分析：回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
    同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：
'''
# for循环调用自定义generator
for n in fib(10):
    print(n)

'''
    # 分析：但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
'''
g = fib(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

'''
    #注：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator。
    特别注意：这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''