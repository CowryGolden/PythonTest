#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 错误、调试和测试-调试：断言（assert）的使用
    # 使用场景：
        调试bug的手段：
        1、第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看；用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。
        2、使用断言；凡是用print()来辅助查看的地方，都可以用断言（assert）来替代；
'''
# 使用断言（assert）
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

if '__main__' == __name__:
    main()    

'''
    #注：运行分析：
    如果断言失败，assert语句本身就会抛出AssertionError：
        运行结果：
        Traceback (most recent call last):
        ......
        AssertionError: n is zero!
    程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：
        E:\XXX\> python -O bug_debug_assert_test1.py
        运行结果：
        Traceback (most recent call last):
        ......
        ZeroDivisionError: division by zero    
    关闭后，你可以把所有的assert语句当成pass来看。
        
'''