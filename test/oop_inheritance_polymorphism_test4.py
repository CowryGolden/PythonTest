#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP-继承和多态（inheritance and polymorphism）：继承、多态练习
    # 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
'''
# 学生类
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name    
    def set_name(self, name):
        self.__name = name

    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        self.__gender = gender  

    def run(self):
        print('Student is running...')
# 男学生类
class Boy(Student):
    def __init__(self, name, gender, love):
        Student.__init__(self, name, gender)
        self.__love = love

    def get_gender(self):
        return super().get_gender() + '-M'    # 直接使用self.__gender，会报错：AttributeError: 'Boy' object has no attribute '_Boy__gender'（原因：子类调用父类的初始化方法，因此子类不能存在自己的私有__gender属性）

    def get_love(self):
        return self.__love

    def run(self):
        print('Boy student is running...')
# 女学生类
class Girl(Student):
    def get_gender(self):
        return super().get_gender() + '-F'      

    def run(self):
        print('Girl student is running...')  
# 猫类
class Cat(object):
    def run(self):
        print('Cat is running...')
# 运行两次run方法
def run_twice(student):
    student.run()
    student.run()

A=Student('Jobs','Male')
B=Boy('Jack','Male','Foorball')
C=Girl('Jane','Famale')
D=Cat()
print(A.get_name(), A.get_gender(), '\n', B.get_name(), B.get_gender(), B.get_love(), '\n', C.get_name() ,C.get_gender())
B.set_gender('Female')
print(B.get_gender())
run_twice(A)
run_twice(C)
run_twice(D)


'''
    #注：数据封装、继承和多态是面向对象的三大特点(encapsulation, inheritance and polymorphism)
    # 静态语言 vs 动态语言 #
    对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
    对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
        class Timer(object):
            def run(self):
                print('Start...')
    这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

    Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

    # 小结 #
    1、继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
    2、动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

'''