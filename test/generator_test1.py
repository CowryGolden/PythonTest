#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 生成器练习：生成器的遍历
'''
g = (x * x for x in range(10))
for n in g:
    print(n)

'''
    #注：generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
    所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
'''