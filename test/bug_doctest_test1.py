#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 错误、调试和测试-文档调试：re模块示例
    # 使用场景：
        如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码。比如re模块就带了很多示例代码，可以把这些示例代码在Python的交互式环境下输入并执行，结果与文档中的示例代码显示的一致。                     

'''
# re模块示例
import re

m = re.search('(?<=abc)def', 'abcdef')
print('m.group(0) =', m.group(0))


'''
    #注：


'''