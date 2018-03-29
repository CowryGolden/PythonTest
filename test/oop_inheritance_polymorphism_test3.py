#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP-继承和多态（inheritance and polymorphism）：多态
    # 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
'''
# 比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
class Animal(object):
    def run(self):
        print('Animal is running...')
# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
# 当然，子类可以对父类方法进行重写，也可以对子类增加一些方法，比如Dog类：
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    
    def eat(self):
        print('Dog is eating meat...')

# 对父类run方法进行重写
class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

print('--------')
# 多态的理解和解释
# 要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
# 判断一个变量是否是某个类型可以用isinstance()判断：
print('isinstance(a, list) =', isinstance(a, list))
print('isinstance(b, Animal) =', isinstance(b, Animal))
print('isinstance(c, Dog) =', isinstance(c, Dog))
# 但是c不仅仅是Dog，c还是Animal！
print('isinstance(c, Animal) =', isinstance(c, Animal))

# 理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())    

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise()) 
# 你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

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