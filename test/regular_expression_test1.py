#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 正则表达式：练习
    # 使用场景：
        请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
            someone@gmail.com
            bill.gates@microsoft.com

'''
# 验证email的合法性
import re

def is_valid_email(addr):
    re_email = re.compile(r'^([a-zA-Z0-9\.]+)@([a-zA-Z0-9]+)\.([a-zA-Z]{2,3})$')
    if re_email.match(addr):
        print(re_email.match(addr).groups())    # 测试
        return True
    else:
        return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

r'''
    #注：

'''