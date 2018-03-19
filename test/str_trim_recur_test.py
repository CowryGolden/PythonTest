#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 练习：利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法。利用递归实现如下：
'''
def trim(s):
    if s == '':
        return s
    elif s[:1] == ' ':  #直接访问s[0]会判断越界，而切片s[:1]不会判断越界的问题
        return trim(s[1:]) #第一个字符为空，就将第一个之后的所有字符作为一个整体进行同样的迭代，直至遇到第一个不为空为止
    elif s[-1:] == ' ':
        return trim(s[:-1]) #最后一个字符为空，就将最有一个前所有字符作为一个整体进行同样的迭代，直至遇到最后一个不为空为止
    else:
        return s

print("trim('hello  ') =",trim('hello  '))
print("trim('  hello') =",trim('  hello'))
print("trim('  hello  ') =",trim('  hello  '))
print("trim('  hello  world  ') =",trim('  hello  world  '))
print("trim('') =",trim(''))
print("trim('    ') =",trim('    '))

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

'''
    #注：
'''