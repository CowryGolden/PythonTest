#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 练习
names=[]
while len(names)<=2:#空列表执行一次，所以+1
    name_number=len(names)+1
    name=input("请输入姓名%d："%name_number)
    names.append(name)
print()
for name in names:#name 与上述含义不同，重新定义
    name_prints=(('hello',name,'!'),)#转换为2维
    for name_print in name_prints:
        print(name_print)
    print()