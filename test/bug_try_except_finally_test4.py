#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    # 错误、调试和测试-错误处理：调用栈
    # 使用场景：
        查看调用层级。如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
'''
# 例子：定义函数main()调用foo()，foo()调用bar()
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')    # 不进行异常捕获
    # try:
    #     bar('0')
    # except Exception as e:
    #     print('Error:', e)
    # finally:
    #     print('finally...')            

if __name__ == '__main__':
    main()

'''
执行打印出的堆栈：
Traceback (most recent call last):
  File "e:\PythonWorkspace\test\bug_try_except_finally_test4.py", line 25, in <module>
    main()
  File "e:\PythonWorkspace\test\bug_try_except_finally_test4.py", line 16, in main
    bar('0')    # 不进行异常捕获
  File "e:\PythonWorkspace\test\bug_try_except_finally_test4.py", line 13, in bar
    return foo(s) * 2
  File "e:\PythonWorkspace\test\bug_try_except_finally_test4.py", line 10, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero

# 错误堆栈解析：
出错并不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键。我们从上往下可以看到整个错误的调用函数链：
    错误信息第1行：
        Traceback (most recent call last):
    告诉我们这是错误的跟踪信息。
    第2~3行：
        File "e:\PythonWorkspace\test\bug_try_except_finally_test4.py", line 25, in <module>
            main()    
    调用main()出错了，在代码文件bug_try_except_finally_test4.py的第25行代码，但原因是第16行： 
        File "e:\PythonWorkspace\test\bug_try_except_finally_test4.py", line 16, in main
            bar('0')    # 不进行异常捕获  
    调用bar('0')出错了，在代码文件bug_try_except_finally_test4.py的第16行代码，但原因是第13行： 
        File "e:\PythonWorkspace\test\bug_try_except_finally_test4.py", line 13, in bar
            return foo(s) * 2
    调用return foo(s) * 2出错了，在代码文件bug_try_except_finally_test4.py的第13行代码，但原因是第10行：     
        File "e:\PythonWorkspace\test\bug_try_except_finally_test4.py", line 10, in foo
            return 10 / int(s)   
    原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了：
        ZeroDivisionError: division by zero    
    根据错误类型ZeroDivisionError，我们判断，int(s)本身并没有出错，但是int(s)返回0，在计算10 / 0时出错，至此，找到错误源头。

    ****  特别强调：出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。****
'''

'''
    #注：Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
        https://docs.python.org/3/library/exceptions.html#exception-hierarchy

#### Exception hierarchy ####
The class hierarchy for built-in exceptions is:
-----------------------------------------------
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning

'''