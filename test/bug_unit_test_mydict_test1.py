#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 错误、调试和测试-调试：单元测试
    # 使用场景：
        以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。
        # 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
        # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
        # 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：
            self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
        # 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
            with self.assertRaises(KeyError):
                value = d['empty']        
        # 而通过d.empty访问不存在的key时，我们期待抛出AttributeError：
            with self.assertRaises(AttributeError):
                value = d.empty                

'''
# 为了编写bug_unit_test_mydict.py(注意模块文件名不能以test结尾)中Dict的单元单元测试，需要引入Python自带的unittest模块

import unittest
from bug_unit_test_mydict import Dict

# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
# 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：
class TestDict(unittest.TestCase):
    
    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value' 
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')   

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty           

### 运行单元测试
# 一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在bug_unit_test_mydict_test1.py的最后加上两行代码：
if __name__ == '__main__':
    unittest.main()


'''
    #注：本单元测试另外的运行方式：
        1、把bug_unit_test_mydict_test1.py当做正常的python脚本运行：
            $ python bug_unit_test_mydict_test1.py
        2、另一种方法是在命令行通过参数-m unittest直接运行单元测试：
            $ python -m unittest bug_unit_test_mydict_test1.py    
        【以上是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。】


'''