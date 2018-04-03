#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 错误、调试和测试-错误处理：抛出错误(raise XXXException)并捕获异常（except），处理异常或继续往上抛异常
    # 使用场景：
        作业：根据抛出的异常进行bug修复
'''
# 作业：分析错误堆栈进行bug修复
from functools import reduce
'''
# 有错误代码如下
def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
'''
# 修复后的代码如下：
def str2num(s):
    return eval(s) # eval函数就是实现list、dict、tuple、int、float等与str之间的转化    #return float(s)    # 也可以换为如下代码
    # if '.' in s:
    #     return float(s)
    # else:
    #     return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

print('eval(\'100 + 200 + 345\') =', eval('100 + 200 + 345'))
print('eval(\'99 + 88 + 7.6\') =', eval('99 + 88 + 7.6'))

'''
    #注：
'''