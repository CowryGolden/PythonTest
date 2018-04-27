#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # 电子邮件-SMTP发送邮件：加密SMTP
    # 使用场景：
        使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
        某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。
        必须知道，Gmail的SMTP端口是587，因此，修改代码如下：

'''
# 使用Gmail的SSL加密SMTP服务
from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
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
smtp_server = 'smtp.gmail.com'    # smtp_server = input('SMTP server: ')
smtp_port = 587   # 其余的默认为：25

# 创建并构造MIMEMultipart邮件对象，代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象
# 利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative
msg = MIMEMultipart('alternative')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)    # msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
msg['Subject'] = Header('来自SMTP的问候，发送同时支持HTML和Plain格式的邮件...... ', 'utf-8').encode()
# 添加纯文本邮件
msg.attach(MIMEText('Hello', 'plain', 'utf-8'))
# 邮件正文是构造HTML通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>,with an image...</p>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取图片
with open('E:\\PythonWorkspace\\test\\test_email.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型
    mime = MIMEBase('image', 'png', filename='test_email.png')
    # 加上必要的头部信息
    mime.add_header('Content-Disposition', 'attachment', filename='test_email.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用Base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, smtp_port)    # Gmail的SMTP端口是587
server.starttls()    # 开启（TLS：Transport Layer Security Protocol；安全传输层协议） 
server.set_debuglevel(1)    # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息；SMTP协议就是简单的文本命令和响应。
server.login(from_addr, password)    # login()方法用来登录SMTP服务器
server.sendmail(from_addr, [to_addr], msg.as_string())  # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
server.quit()


r'''
    #注：

'''