#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 自定义一个关键字参数的函数，允许传入0个或任意多个包含参数名的参数，这些关键字参数在函数内部自动组装成为一个dict。实例如下：
def person(name, age, **kw):
    print('name:',name,'age:',age,'other:',kw)

print("person('Michael',30) =")
person('Michael',30)

print("person('Bob', 35, city='Beijing') =")
person('Bob', 35, city='Beijing')

print("person('Adam', 45, gender='M', job='Engineer') =")
person('Adam', 45, gender='M', job='Engineer')

extra = {'city':'Beijing','job':'Engineer'}
print("person('Jack',24,city=extra['city'],job=extra['job']) =")
person('Jack',24,city=extra['city'],job=extra['job'])
print("person('Jack',24,**extra) =")
person('Jack',24,**extra)

'''
    #注：和可变参数类似，关键字参数可以先组装出一个dict，然后把dict转为关键字参数传进去；
    **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
    注意：kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
'''