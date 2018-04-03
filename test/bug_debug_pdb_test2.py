#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 错误、调试和测试-调试：pdb.set_trace()的使用
    # 使用场景：
    这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。
    pdb.set_trace()

        调试bug的手段：
        1、第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看；用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。
        2、使用断言；凡是用print()来辅助查看的地方，都可以用断言（assert）来替代；
        3、把print替换为logging，和assert比，logging不会抛出错误，而且可以输出到文件；
        4、启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
'''
# pdb.set_trace()的使用
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
import pdb

s = '0'
n = int(s)
pdb.set_trace()    # 运行到这里会自动暂停
print(10 / n)

# python bug_debug_pdb_test2.py运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：

'''
    #注：这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。

'''