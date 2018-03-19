#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-高阶函数-filter练习：求素数
'''
#2一定是一个素数，先构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#注意上述是一个生成器，并且是一个无限序列；再定义一个筛选器
def _not_divisible(n):
    return lambda x: x % n > 0
#最后定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() #初识序列
    while True:
        n = next(it) #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) #构造新序列
#这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
#由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
#打印1000以内的素数
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break
if __name__ == '__main__':
    main()

'''
    #注：注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。
'''