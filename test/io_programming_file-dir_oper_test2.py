#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # IO编程-操作文件和目录：os和os.path模块操作文件和目录
    # 使用场景：
        操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以参考如下调用：
'''
# 对文件路径的拆分，后缀名获取，重命名，删除等操作
import os
# 通过os.path.split()函数，拆分路径（这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名）
f1 = os.path.split('/Users/CowryGolden/testdir/file.txt')
print('f1 =', f1)
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
f2 = os.path.splitext('/Users/CowryGolden/testdir/file.txt')
print('f2 =', f2)
print('文件后缀名为 :', f2[1])
# 【特别说明：】这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# 对文件重命名和删除操作
filepath = 'E:\\PythonWorkspace\\test\\testdir\\test.txt'
renamef = 'E:\\PythonWorkspace\\test\\testdir\\test.py'
if os.path.exists(filepath) and os.path.isfile(filepath):
    fs = os.path.splitext(filepath)
    if fs[1] == '.txt':
        os.rename(filepath, renamef)
        print('文件重命名成功！')
else:
    # os.mknod(filepath) Linux下可以使用该方法创建空文件
    open(filepath, 'w+').close()
    print('文件创建成功！')

if os.path.exists(renamef):
    os.remove(renamef)
    print('文件删除成功！')

r'''
    #注：把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
            part-1/part-2
        而Windows下会返回这样的字符串：
            part-1\part-2
        同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
            >>> os.path.split('/Users/michael/testdir/file.txt')
            ('/Users/michael/testdir', 'file.txt')
        os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
            >>> os.path.splitext('/path/to/file.txt')
            ('/path/to/file', '.txt')
        这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。    

'''