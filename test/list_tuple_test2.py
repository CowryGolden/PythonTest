#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# tuple练习，tuple-元组，有序数据列表，和list类似，但tuple一旦初始化就不能修改了，它也没有append()，insert()，pop()这样的方法。

print('====空tuple:t====')
t = ()
print('====t的内容为====')
print(t)
print('====t的长度为====')
print(len(t))

print('====包含一个元素的tuple:t1====')
t1 = (1,)
print('====t1的内容为====')
print(t1)
print('====t1的长度为====')
print(len(t1))
print('====t1的第0个元素为====')
print(t1[0])

print('====包含多个元素的tuple:t2====')
t2 = ('Michael', 'Bob', 'Tracy')
print('====t2的内容为====')
print(t2)
print('====t2的长度为====')
print(len(t2))
print('====t2的第1个元素为====')
print(t2[1])


print('====定义一个包含list元素的tuple:t3====')
t3 = ('a', 'b', ['A', 'B'])
print('====t3的原始内容为====')
print(t3)
print('====t3的长度为====')
print(len(t3))
print('====更改t3中list的元素的内容====')
t3[2][0] = 'X'
t3[2][1] = 'Y'
print('====更改后的t3内容为====')
print(t3)
