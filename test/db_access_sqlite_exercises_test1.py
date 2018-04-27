#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 访问数据库-SQLite：SQLite使用练习
    # 使用场景：
        请编写函数，在Sqlite中根据分数段查找指定的名字：

'''
# 编写函数，在Sqlite中根据分数段查找指定的名字，按分数从低到高排序
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'db_access_sqlite_exercises_test1.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始化数据库
try:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
except ConnectionError:
    conn.rollback()
    raise ConnectionError('Error occurred')    
finally:
    cursor.close()
    conn.commit()
    conn.close()

def get_score_in(low, high):    # 返回指定分数区间的名字，按分数从低到高排序
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        # 方法一：先查询出符合条件的结果，使用sorted进行排序
        # cursor.execute('select * from user where score between ? and ?', (low, high))
        # values = cursor.fetchall()
        # results = []
        # L = sorted(values, key=lambda x: x[2])
        # print('L =', L)
        # for i in range(len(L)):
        #     results.append(L[i][1])
        # return results

        # 方法二：数据库查询语句中直接使用order by子句进行排序
        cursor.execute('select * from user where score between ? and ? order by score asc', (low, high))
        values = cursor.fetchall()
        print('values =', values)
        results = []
        for i in range(len(values)):
            results.append(values[i][1])
        return results
    except ConnectionError:
        raise ConnectionError('Error occurred')    
    finally:
        cursor.close()
        conn.close()

print('get_score_in(80, 95) =', get_score_in(80, 95)) 
print('get_score_in(60, 80) =', get_score_in(60, 80)) 
print('get_score_in(60, 100) =', get_score_in(60, 100))    

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('---- OK ----')

r'''
    #注：

'''