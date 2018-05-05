#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块：itertools模块，常用函数示例
    # 使用场景：
        Python的内建模块itertools常用模块函数示例

'''
# itertools模块，常用函数示例
import itertools

print('======== 数字的无限迭代 ========')
########## Infinite Iterators: ##########
# 数字的无限迭代
for c in itertools.count(10):
    print(c)
    if c>10:
        break;

print()
print('======== 特定字符的无限迭代 ========')
# 特定字符的无限迭代
a = 0
for c in itertools.cycle('ABCD'):
    print(c)
    a = a + 1
    if a>10:
        break

print()
print('======== 重复特定次数 ========')
# 重复特定次数
for c in itertools.repeat('ABCD',3):
    print(c)


########## Iterators terminating on the shortest input sequence: ##########

print()
print('======== 累积计算(累加和) ========')
# 累积计算
for c in itertools.accumulate([1,2,3,4,5]):
    print(c)

print()
print('======== 合并字符串（itertools.chain(str1, str2, ...)） ========')
# 合并字符串
for c in itertools.chain('ABC', 'DEF'):
    print(c)

print()
print('======== 合并字符串（itertools.chain.from_iterable([str1, str2, ...])） ========')
# 合并字符串
for c in itertools.chain.from_iterable(['ZYX', 'UVW']) :
    print(c)

print()
print('======== 压缩字符串(1位置的输出，0位置不输出) ========')
# 压缩字符串
for c in itertools.compress('ABCDEF', [1,0,1,0,1,1]) :
    print(c)

print()
print('======== 过滤字符串，获得第一次断言是false后的一切元素 ========')
# 过滤字符串
# 获得第一次断言是false后的一切元素
for c in itertools.dropwhile(lambda x: x<5, [1,4,6,4,1,20,50]) :
    print(c)

print()
print('======== 过滤字符串，获得断言是false的元素 ========')
# 过滤字符串
# 获得断言是false的元素
for c in itertools.filterfalse(lambda x: x%2, range(10))  :
    print(c)

print()
print('======== 只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。 ========')
# 只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的，而函数返回值作为组的key。
for c,sub in itertools.groupby('AAABBBCCC', lambda c: c.upper()):
    print(c,list(sub))

print()
print('======== 字符串切片输出（seq, [start,] stop [, step]），如从索引位置为2的位置取到最后 ========')
# seq, [start,] stop [, step]
for c in itertools.islice('ABCDEFG', 2, None):
    print(c)

print()
print('======== 对迭代对象进行指定函数的map操作；如将list中每个tuple的两个元素进行pow()操作 ========')
# func, seq
# func(*seq[0]), func(*seq[1]), ...
for c in itertools.starmap(pow, [(2,5), (3,2), (10,3)]) :
    print(c)    

print()
print('======== takewhile()控制输出用法，输出符合指定限制的内容 ========')
# pred, seq
# seq[0], seq[1], until pred fails
for c in itertools.takewhile(lambda x: x<5, [1,4,6,4,1]) :
    print(c)    

print()
print('======== 一个迭代器变成n个，即将给定的迭代器变为指定数目的n个相同的迭代器 ========')
# 一个迭代器变成n个
# it, n
# it1, it2, ... itn splits one iterator into n
for c in itertools.tee([1,4,6,4,1], 2) :
    print(list(c))

print()
print('======== 将给定的两个迭代器，按照最长的进行组合成元组，不足的以给定的元素内容补充 ========')
# 按照最长的进行组合成元组
for c in itertools.zip_longest('ABCD', 'xy', fillvalue='-'):
    print(c)


########## Combinatoric generators: ##########

print()
print('======== 将给定的迭代器，按指定的集合数目求笛卡尔积 ========')
# 笛卡尔积
# p, q, ... [repeat=1]
for c in itertools.product('ABCD', repeat=2):
    print(c)

print()
print('======== 将给定的迭代器，按指定的集合数目求全排列（即，去除笛卡尔积中自身和自身的排列，顺序不同即不同） ========')
# 返回r长度的元素的排列
# Return successive r length permutations of elements in the iterable.
# successive 逐次; 连续的，相继的; 继承的，接替的; 
# permutations 序列，排列，排列中的任一组数字或文字
for c in itertools.permutations('ABCD', 2):
    print(c)

print()
print('======== 将给定的迭代器，按指定的集合数目求组合（即，去除排列中组合相同的；即内容相同顺序不同，算一个） ========')
# r长度的元素的组合，元素不重复
for c in itertools.combinations('ABCD', 2):
    print(c)


print()
print('======== 将给定的迭代器，按指定的集合数目求全组合，允许自身和自身组合，即允许组合元素内容相同（即，在上述组合中加上自身与自身的组合） ========')
# r长度的元素的组合，允许重复
for c in itertools.combinations_with_replacement('ABCD', 2):
    print(c)

r'''
    #注：

'''