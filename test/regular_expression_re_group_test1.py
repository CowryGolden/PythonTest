#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 正则表达式：re模块group练习
    # 使用场景：
        除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：
        ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：

'''
# re模块的使用
import re

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print('m =', m)
print('m.group(0) =',m.group(0))
print('m.group(1) =',m.group(1))
print('m.group(2) =',m.group(2))

r'''
    #注：如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
        注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。

'''