#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 练习：请使用迭代查找一个list中最小和最大值，并返回一个tuple：
'''
def findMinAndMax(L):
    if len(L) != 0:
        min = max = L[0]
        for x in L:
            if x > max:
                max = x
            elif x < min:
                min = x
    else:
        min = max = None
    return (min,max)    

print('findMinAndMax([]) =',findMinAndMax([]))
print('findMinAndMax([7]) =',findMinAndMax([7]))
print('findMinAndMax([7, 1]) =',findMinAndMax([7, 1]))
print('findMinAndMax([7, 1, 3, 9, 5]) =',findMinAndMax([7, 1, 3, 9, 5]))

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

'''
    #注：
'''