#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-使用元类：type()的使用
    # 使用场景：
        *** 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
        *** type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义；
            实际使用的就是type.__new__()来创建的；具体例子如下：
'''
# 定义函数
def fn(self, name = 'world'):
    print('Hello, %s.' % name)

# 利用type()动态创建Hello class
Hello = type('Hello', (object,), dict(hello = fn))
# 注意上述语句中第二个(object,)为一个元组tuple，为只有一个父类的写法，不能写成(object)或object，否则会报错：TypeError: type.__new__() argument 2 must be tuple, not type

# 测试
h = Hello()
h.hello()

print('type(Hello) =', type(Hello))
print('type(h) =', type(h))
'''
    执行结果：
        Hello, world.
        type(Hello) = <class 'type'>
        type(h) = <class '__main__.Hello'>

'''

'''
    #注：关于使用type()的用法：（可使用help(type)查看用法及参数解释）
    class type(object)
        type(object_or_name, bases, dict)
        type(object) -> the object's type
        type(name, bases, dict) -> a new type

        Data and other attributes defined here:
            |  __base__ = <class 'object'>
            |      The most base type
            |
            |  __bases__ = (<class 'object'>,)    # 注意__bases__属性为元组tuple，可以列出需要继承的类的类型
    
    总结：
        要创建一个class对象，type()函数依次传入3个参数：
        1、class的名称；
        2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法：(object,)；
        3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
    通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

    正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

'''