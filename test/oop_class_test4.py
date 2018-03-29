#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP(Object Oriented Programming)：访问控制（将类属性变量变为私有属性（private））
    在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。
'''
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name  

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad score')    
    def get_score(self):
        return self.__score      

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 75:
            return 'B'
        elif self.__score >= 60:
            return 'C'    
        else:
            return 'D'
 
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
emliy = Student('Emily', 100)
print(lisa.get_name(), lisa.get_score(), lisa.get_grade())
print(bart.get_name(), bart.get_score(), bart.get_grade())
print(emliy.get_name(), emliy.get_score(), emliy.get_grade())
#emliy.set_score(105)

'''
    #注：数据封装、继承和多态是面向对象的三大特点

    1、在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。
    2、需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
    3、有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
    4、双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
        >>> bart._Student__name
        'Bart Simpson'
       （特别注意：但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。）
       总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

'''