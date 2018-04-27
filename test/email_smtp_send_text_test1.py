#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 电子邮件-SMTP发送邮件：发送纯文本邮件
    # 使用场景：
        SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
        Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
        首先，我们来构造一个最简单的纯文本邮件：

'''
# 构造一个简单的纯文本邮件并发送出去
from email.mime.text import MIMEText
import smtplib

msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，
# 最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。然后通过SMTP发出去：

# 输入Email地址和口令
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址
to_addr = input('To: ')
# 输入SMTP服务器地址，如：smtp.163.com
smtp_server = input('SMTP server: ')

server = smtplib.SMTP(smtp_server, 25)    # SMTP协议默认端口是25
server.set_debuglevel(1)    # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息；SMTP协议就是简单的文本命令和响应。
server.login(from_addr, password)    # login()方法用来登录SMTP服务器
server.sendmail(from_addr, [to_addr], msg.as_string())  # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
server.quit()


r'''
    #注：如果一切顺利，就可以在收件人信箱中收到我们刚发送的Email：【事实证明，缺失主题等信息无法发送出去。】
        仔细观察，发现如下问题：
            1、邮件没有主题；
            2、收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>；
            3、明明收到了邮件，却提示不在收件人中。
        这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：    

'''