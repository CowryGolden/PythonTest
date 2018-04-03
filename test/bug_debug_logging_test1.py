#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 错误、调试和测试-调试：logging的使用
    # 使用场景：
        调试bug的手段：
        1、第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看；用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。
        2、使用断言；凡是用print()来辅助查看的地方，都可以用断言（assert）来替代；
        3、把print替换为logging，和assert比，logging不会抛出错误，而且可以输出到文件；
'''
# logging使用

'''
import logging
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
以上代码输出结果：
Traceback (most recent call last):
  File "e:\PythonWorkspace\test\bug_debug_logging_test1.py", line 17, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
'''
# logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。怎么回事？
# 别急，在import logging之后添加一行配置再试试：
import logging
logging.basicConfig(level = logging.INFO)  # logging.WARN/DEBUG

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

'''
    #注：运行分析：
    运行结果：
        INFO:root:n = 0
        Traceback (most recent call last):
        File "e:\PythonWorkspace\test\bug_debug_logging_test1.py", line 33, in <module>
            print(10 / n)
        ZeroDivisionError: division by zero    
    这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
    当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，
    debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，
    最后统一控制输出哪个级别的信息。
    logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

'''