#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 常用內建模块-collections集合模块：deque的使用
    # 使用场景：
        使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
        deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

'''
# 使用deque进行列表（队列或栈）的增删改查
from collections import deque

d = deque(['a', 'b', 'c'])
print('d =', d)
d.append('x')    # 在队列最右边（末尾）增加元素
print('d =', d)
d.appendleft('y')    # 在队列最左边（头部）增加元素
print('d =', d)
d.pop()    # 删除队列最右边（末尾）元素
print('d =', d)
d.popleft()    # 删除队列最左边（头部）元素
print('d =', d)


r'''
    #注：deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

'''