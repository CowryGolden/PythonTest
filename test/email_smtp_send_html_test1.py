#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 电子邮件-SMTP发送邮件：发送HTML邮件
    # 使用场景：
        SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
        Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
        在发送邮件的文本中添加邮件主题、发件人、收件人等信息，把From、To和Subject添加到MIMEText中，才是一封完整的邮件
        如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：

'''
# 构造一个简单的html邮件并发送出去
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# 编写了一个函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，
# 最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。然后通过SMTP发出去：

# 输入Email地址和口令
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址
to_addr = input('To: ')
# 输入SMTP服务器地址，如：smtp.163.com
smtp_server = input('SMTP server: ')

# 在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以发送HTML邮件了
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)    # msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
msg['Subject'] = Header('来自SMTP的问候，发送HTML邮件...... ', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)    # SMTP协议默认端口是25
server.set_debuglevel(1)    # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息；SMTP协议就是简单的文本命令和响应。
server.login(from_addr, password)    # login()方法用来登录SMTP服务器
server.sendmail(from_addr, [to_addr], msg.as_string())  # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
server.quit()


r'''
    #注：

'''