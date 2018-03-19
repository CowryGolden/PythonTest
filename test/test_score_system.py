#!/usr/bin/env python3
# -*- coding: utf-8 -*-

resould = {}
while True:
    num = int( input('''
请输入您要的序号:
  1.成绩查询
  2.成绩录改
  3.成绩删除
  4.列出所有人成绩
  其他任意键退出:\n''') )
    if num == 1:
        name = input('请输入您要查询的姓名:\n')
        if name in resould:
            print('%s的成绩为：%s分'%(name,resould[name]) )
        else:
            print('查无此人')
    elif num == 2:
        name1 = input('请输入您要录入的姓名:\n')
        num1 = int(input('请输入%s的分数:\n'%name1) )
        resould[name1] = num1
    elif num == 3:
        name1 = input('请输入您要删除的姓名:\n')
        if name1 in resould:
            print(resould.pop(name1))
        else:
            print('对不起，查无此人')
    elif num == 4:
        print(resould)
    else:
        break
print('系统退出')