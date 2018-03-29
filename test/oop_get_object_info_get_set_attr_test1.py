#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP-获取对象信息：hasattr(),getattr(),setattr()等方法的使用

'''
# 首先你可以将如下MyObject类放于command.py文件（这里就放于同一个文件中了），内容如下，这里我们假若它后面还有100个方法
class MyObject(object):
    def __init__(self):
        self.x = 9
    def add(self):
        return self.x + self.x

    def pow(self):
        return self.x * self.x

    def sub(self):
        return self.x - self.x

    def div(self):
        return self.x / self.x

'''
# 然后我们有一个入口文件 exec.py（这里就放于同一个文件中了），要根据用户的输入来执行后端的操作
# from command import MyObject #（上述MyObject类放于单独的command.py文件中打开注释使用）

computer=MyObject()
def run():
    inp = input('method>')

    if inp == 'add':
        computer.add()
    elif inp == 'sub':
        computer.sub()
    elif inp == 'div':
        computer.div()
    elif inp == 'pow':
        computer.pow()
    else:
        print('404')

# 上面使用了if来进行判断，那么假若我的command里面真的有100个方法，那我总不可能写100次判断吧，所以这里我们就会用到python的反射特性，看下面的代码:
'''
# from command import MyObject #（上述MyObject类放于单独的command.py文件中打开注释使用）

computer=MyObject()
def run(x):
    inp = input('method >>>')
    # 判断是否有这个属性
    if hasattr(computer, inp):
    # 有就获取然后赋值给新的变量
        func = getattr(computer, inp)
        print(func())
    else:
    # 没有我们来set一个
        setattr(computer, inp, lambda x:x+1)
        func = getattr(computer, inp)
        print(func(x))

if __name__ == '__main__':
    run(10)

'''
    #注：
'''