#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 自定义函数练习：计算一个或多个数的乘积，参数为空异常处理      
'''
def product(*nums):
    m = 1
    if (nums is None) or (len(nums) == 0):
        m = None
        raise TypeError('invalid value:%s' % m)
    for x in nums:
        m = m * x    
    return m

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

'''
    #注：
'''