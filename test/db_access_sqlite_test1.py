#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 访问数据库-SQLite：使用SQLite
    # 使用场景：
        SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
        Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
        在使用SQLite前，我们先要搞清楚几个概念：
            表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
            要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
            连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。

        Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
        由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。

'''
# 在Python中操作SQLite数据库，创建一个user表，并插入一条数据
# 先导入SQLite驱动
import sqlite3

# 连接到SQLite数据库
# 数据库文件是db_access_sqlite_test.db
# 如果文件不存在，会自动在当前目录创建：
conn = sqlite3.connect('db_access_sqlite_test.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条sql语句，创建user表(创建前如果存在先drop)
# cursor.execute('drop table user')
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数
print('cursor.rowcount =', cursor.rowcount)
# 关闭Cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection
conn.close()

r'''
    #注：

'''