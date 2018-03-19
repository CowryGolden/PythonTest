#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list练习，list是一个可变的有序表，因此可以对list进行增删改查
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print('====原始L：====')
print(L)

print('====L.append(?) list是一个可变的有序表，在list末尾追加元素====')
L.append('Test')
print(L)

print('====L.insert(index, ?) 把元素插入到指定的位置，index为索引位置====')
L.insert(1,'List')
print(L)

print('====L.pop() 删除list末尾的元素====')
L.pop()
print(L)

print('====L.pop(index) 删除指定位置的元素，index为索引位置====')
L.pop(1)
print(L)

print('====L当前的长度为：====')
print(len(L))

print('====获取list指定位置元素内容====')
# 打印Apple:
print('L[0][0]=' + L[0][0])
# 打印Python:
print('L[1][1]=' + L[1][1])
# 打印Lisa:
print('L[2][2]=' + L[2][2])