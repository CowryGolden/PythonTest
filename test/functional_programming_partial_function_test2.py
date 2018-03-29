#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 函数式编程-偏函数练习：利用偏函数，进行2进制转10进制；8进制转10进制，16进制转10进制

'''
import functools
#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
int2 = functools.partial(int, base = 2)
int8 = functools.partial(int, base = 8)
int16 = functools.partial(int, base = 16)

print("int2('1010101') =", int2('1010101'))
print("int8('12345670') =", int8('12345670'))
print("int16('1234567890ABCDEF') =", int16('1234567890ABCDEF'))

'''
    #注：以上如果不使用偏函数，自定义函数为：
        def int2(x, base = 2):
            return int(x, base)
        
        偏函数：int2 = functools.partial(int, base = 2)
        其中int2('101010')
        相当于：
            kw = {'base' : 2}
            int('101010', **kw)
    #再如：偏函数 max2 = functools.partial(max, 10)
        实际上会把10作为*args的一部分自动加到左边，也就是：
            max2(5, 6, 7)
        相当于：
            args = (10, 5, 6, 7)
            max(*args)
        结果为：10
    #小结：
        当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''