#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # Python图形化界面（GUI）：Tkinter的使用，练习
    # 使用场景：
        开发一个很简陋的BMI换算器，计算公式：BMI = float(weigh) / (float(high) * 2)  【注：体重单位：kg，身高单位：m】

'''
# 开发一个很简陋的BMI换算器
from tkinter import *
import tkinter.messagebox as messagebox

def BMI(high,weigh):
    check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for i in list(high):
        if i not in check:
            return ("参数输入有误，请输入数字。")

    for i in list(weigh):
        if i not in check:
            return ("参数输入有误，请输入数字。")

    if not high or not weigh:
        return None

    BMI =  float(weigh) / (float(high) * 2)

    if BMI < 18.5 :
        return ('您的BMI指数为%.2f，您的身体情况属于过轻。' % BMI)
    elif BMI < 24:
        return ('您的BMI指数为%.2f，您的身体情况属于正常。' % BMI)
    elif BMI < 28:
        return ('您的BMI指数为%.2f，您的身体情况属于过重。' % BMI)
    elif BMI <= 32:
        return ('您的BMI指数为%.2f，您的身体情况属于肥胖。' % BMI)
    else:
        return ('您的BMI指数为%.2f，您的身体情况属于严重肥胖。' % BMI)

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.label1 = Label(self,text = '请输入您的身高(m):')
        self.label1.pack()
        self.nameInput1 = Entry(self)
        self.nameInput1.pack()
        self.label2 = Label(self,text = '请输入您的体重(kg):')
        self.label2.pack()
        self.nameInput2 = Entry(self)
        self.nameInput2.pack()
        self.alertButton = Button(self,text='点击显示结果',command = self.result)
        self.alertButton.pack()

    def result(self):
        BMI_result = BMI(self.nameInput1.get(),self.nameInput2.get()) or '请输入您的参数'
        messagebox.showinfo("BMI转换结果",'%s' % BMI_result )



if __name__ == '__main__':
    app = Application()
    app.master.title("BMI转换器")
    app.mainloop()     

r'''
    #注：

'''