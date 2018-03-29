#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # OOP高级编程-使用元类：metaclass的使用，实现简单ORM框架，定义一个User类来操作对应的数据库表User
    # 使用场景：
        ORM就是一个典型的例子，通过metaclass修改类定义的。
        ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
        要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
        让我们来尝试编写一个ORM框架。
        编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User。
'''
'''
# 我们期待的用户调用代码为：
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例
user = User(id=101001, name = 'Michael', email = 'test@orm.org', password = 'my-pwd')
# 保存到数据库
user.save()
'''
# 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如save()全部由metaclass自动完成。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。
# 现在，我们就按上面的接口来实现该ORM。
# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name    # 字段名
        self.column_type = column_type    # 字段类型

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)    # 实际的数据类型类和字段名（数据库字段名=类或实例属性名）

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')    # 字段名和字段类型

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')    # 字段名和字段类型

# 下一步，就只编写最复杂的ModelMetaclass了：
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):   # cls: 正在被生成的对象, name: 生成该对象的类名, bases: 父类集合, attrs: 属性方法集合
        if name == 'Model':    # 若类名为Model, 则是对Model的修改，原样返回
            return type.__new__(cls, name, bases, attrs) 
        print('Found model: %s' % name)
        mappings = dict()    # 初始化属性方法字典
        # 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Fount mapping: %s ==> %s' % (k, v))    # 输出属性类型和属性名
                mappings[k] = v    # 将属性类型(key)和属性名(value)加入到字典
        for k in mappings.keys():
            attrs.pop(k)    # 类属性中删除该Field属性, 否则容易造成运行时错误(实例的属性会遮盖类的同名属性)

        attrs['__mappings__'] = mappings    # 保存属性和列的映射关系
        attrs['__table__'] = name    # 这里假设表名和列名一致
        return type.__new__(cls, name, bases, attrs)

# 定义基类Model
class Model(dict, metaclass = ModelMetaclass):    # 使用ModelMetaclass来创建类
    def __init__(self, **kw):    # **kw命名关键词参数
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):    # 获得values
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):    # 设置属性/方法名
        self[key] = value

    def save(self):    # 将属性保存到数据库(此处仅为生成相应的SQL语句)
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)    # 将字段名加入到fields中
            params.append('?')    # 向params中添加xxx个问号
            args.append(getattr(self, k, None))    # 将values加入args中
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))   # 生成SQL语句, join方法是将list中的内容以前面的符号作为分隔连在一起 
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# 有了基类Model，定义User类
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例
user = User(id=101001, name = 'Michael', email = 'test@orm.org', password = 'my-pwd')
# 保存到数据库
user.save()

'''
    #注：总结：
        当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，如果没有找到，就继续在父类Model中查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。
        在ModelMetaclass中，一共做了几件事情：
            1、排除掉对Model类的修改；
            2、在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
            3、把表名保存到__table__中，这里简化为表名默认为类名。
        在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。
        我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。

    #### 关于line:59为什么要将类中Field属性删除attrs.pop(key) ####
    为什么要删除类中的Field属性attrs.pop(key)。元类用于创建类的时候，元类的new方法先于被创建类的init()方法。
    当u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')时，
    首先建立User类里头有属性id，name(但此时并没有创建出类的实例)等，由于Model是User类父类，
    而Model类使用了元类，故先调用的方法为元类中new()。以id为例，在mappings字典中此时建立的
    应该是{id:IntegerField('id')}。假设没有attrs.pop()那么在调用u.save()时，getattr()
    首先从类的属性或者父类的属性中找，只有查询不到时，才会到getattrs中查找。由于没有把原本的
    id关键字弹出，故getattr便能从类的属性id=IntegerField得到IntegerField。一旦有了
    attrs.pop()在类中就查询不到相应的属性，那么就要调用getattrs而返回值是self[k],由于
    self不是指类而是类的实例，所以能够成功返回，构建实例时创建id的值12345，这样就正确得到传入的实参值。


'''