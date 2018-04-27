#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 访问数据库-SQLAlchemy：使用SQLAlchemy练习
    # 使用场景：
        由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
        例如，如果一个User拥有多个Book，就可以定义一对多关系如下：
            class User(Base):
                __tablename__ = 'user'

                id = Column(String(20), primary_key=True)
                name = Column(String(20))
                # 一对多:
                books = relationship('Book')

            class Book(Base):
                __tablename__ = 'book'

                id = Column(String(20), primary_key=True)
                name = Column(String(20))
                # “多”的一方的book表是通过外键关联到user表的:
                user_id = Column(String(20), ForeignKey('user.id'))    
        当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。                     

'''
# 使用SQLAlchemy进行关系数据库表“一对多”关系练习
# 导入依赖模块:
import json
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    book = relationship('Book')

    def __str__(self):
        return 'user: id = %s,name = %s,books=%s' % (self.id, self.name, self.book)

    __repr__ = __str__


def tojson(self):
    if isinstance(self, User):
        return {
            'id': self.id,
            'name': self.name,
            'book': self.book
        }
    else:
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id
        }

class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey('user.id'))

    def __str__(self):
        return 'book: id = %s,name = %s,user_id = %s' % (self.id, self.name, self.user_id)

    __repr__ = __str__

engine = create_engine('mysql+mysqlconnector://root:r00t@localhost:3306/testdb')
DBSession = sessionmaker(bind=engine)

# session=DBSession()
# new_user=User(id = '5',name = 'Bob')
# session.add(new_user)
# session.commit()
# session.close()

session = DBSession()
users = session.query(User).all()
print('user type :', type(users))
# print('id :',user.id)
# print('name :',user.name)
for u in users:
    # print('book type :',type(u.book))
    print(u)
print(users)
print('---------------------------')
u = session.query(User).filter(User.id == '10005').one()
print(u)
print(json.dumps(users, default=tojson,indent=4))

r'''
    #注：需要提前创建book表，并设置外键：
            # 导入MySQL驱动:
            import mysql.connector
            # 注意把password设为你的root口令:
            conn = mysql.connector.connect(user='root', password='r00t', database='testdb')
            cursor = conn.cursor()
            # 创建user表:
            cursor.execute('create table if not exists user (id varchar(20) primary key, name varchar(20))')
            # 创建book表:
            cursor.execute('create table if not exists book (id varchar(20) PRIMARY KEY, name varchar(20),user_id VARCHAR (20),FOREIGN KEY (user_id) REFERENCES user(id))')
            # 插入一行记录，注意MySQL的占位符是%s:
            # cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
            cursor.rowcount
            # 提交事务:
            conn.commit()
            cursor.close()
            # 运行查询:
            cursor = conn.cursor()
            cursor.execute('select * from user ')
            values = cursor.fetchall()
            print(values)

            # 关闭Cursor和Connection:
            cursor.close()
            conn.close()

'''