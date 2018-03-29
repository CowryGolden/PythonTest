#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-multi继承（multi inheritance）：多重继承练习；关于多重继承的查询顺序理解（可以通过__mro__属性获取继承线性序列）
    原文链接：https://kevinguo.me/2018/01/19/python-topological-sorting/
'''
# 通过__mro__属性获取继承的线性序列，理解C3算法
class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A,B):
    pass

class C2(A,B):
    def bar(self):
        print('C2-bar')

class D(C1,C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo()
    d.bar()
'''
执行结果：
    (<class '__main__.D'>, <class '__main__.C1'>, <class '__main__.C2'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
    A foo
    C2-bar
'''
'''
    #注：关于多重继承,其实,只要了解拓扑排序,就能很清楚的指导多重继承的查询顺序了,从入度为0的位置起,剪掉入度为0相关边,然后接着找下一个入度为0的位置,如此往复到最后,遇到有多个入度为0的时候,按最左原则取就行了。
    在图论中，拓扑排序(Topological Sorting) 是一个 有向无环图(DAG,Directed Acyclic Graph) 的所有顶点的线性序列。且该序列必须满足下面两个条件：
        1、每个顶点出现且只出现一次。
        2、若存在一条从顶点A到顶点B的路径，那么在序列中顶点A出现在顶点B的前面。
    最后，python继承顺序算法（MRO算法：Method Resolution Order）遵循C3算法，只要在一个地方找到了所需的内容，就不再继续查找。可以通过__mro__属性获取继承线性序列。
'''