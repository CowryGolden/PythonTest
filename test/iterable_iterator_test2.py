#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 迭代器练习：关于for循环的迭代器解释
'''
#Python的for循环本质上就是通过不断调用next()函数实现的。例如：
print('==== for循环实现 ====')
for x in [1,2,3,4,5]:
    print(x)
print('==== 迭代器实现 ====')
#首先获得Iterator对象
it = iter([1,2,3,4,5])
#循环
while True:
    try:
        #获得下一个值
        x = next(it)
        print(x)
    except StopIteration:
        #遇到StopIteration就退出循环
        break


'''
    #总结：
        1、凡是可作用于for循环的对象都是Iterable类型；
        2、凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
        3、集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
    #特别注意：
        isinstance((x for x in range(10)), Iterator)为true
        但是isinstance([x for x in range(10)], Iterator)为false
        注意：(x for x in range(10)创建的是一个generator，[x for x in range(10)]创建的是一个列表list
        【参见生成器生成方式：只要把一个列表生成式的[]改成()，就创建了一个generator】
'''