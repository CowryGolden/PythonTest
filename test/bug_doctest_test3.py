#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 错误、调试和测试-文档调试：文档测试（doctest）练习
    # 使用场景：
        如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码。比如re模块就带了很多示例代码，可以把这些示例代码在Python的交互式环境下输入并执行，结果与文档中的示例代码显示的一致。                     
        并且，Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
        doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。
'''
# 对函数fact(n)编写doctest并执行，如下为修改前源代码，请修改后让文档测试通过：
r'''
def fact(n):
    \'''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    ?
    >>> fact(-1)
    ?
    \'''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

# 以上为修改前的代码，其运行结果如注释中所示：
'''

def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: n不能为负数n = -1
    '''
    
    if n < 1:
        raise ValueError('n不能为负数n = %d' % n)    
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()        

r'''
    #注：修改前的运行结果如下所示：

********************************************************************** 
File "C:\Users\GOLDEN~1\AppData\Local\Temp\learn_python_fly82euj_py\test_1.py", line 8, in __main__.fact 
Failed example: 
    fact(10) 
Expected: 
    ? 
Got: 
    3628800 
********************************************************************** 
File "C:\Users\GOLDEN~1\AppData\Local\Temp\learn_python_fly82euj_py\test_1.py", line 10, in __main__.fact 
Failed example: 
    fact(-1) 
Exception raised: 
    Traceback (most recent call last): 
      File "D:\ProgramFiles\Python364\lib\doctest.py", line 1330, in __run 
        compileflags, 1), test.globs) 
      File "<doctest __main__.fact[2]>", line 1, in <module> 
        fact(-1) 
      File "C:\Users\GOLDEN~1\AppData\Local\Temp\learn_python_fly82euj_py\test_1.py", line 14, in fact 
        raise ValueError() 
    ValueError 
********************************************************************** 
1 items had failures: 
   2 of   3 in __main__.fact 
***Test Failed*** 2 failures. 

'''