#!/usr/bin/env python3
# coding:utf-8
# 代码6-8email01.py

# 导入需要用到的库
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 设置SMTP服务器和端口，这里以QQ邮箱为例
host = "smtp.qq.com"
port = 465

# 发送邮件的QQ号和SMTP授权码，需要先在QQ邮箱中开启SMTP服务并获取授权码
user = "642825572"
code = "ecruzodsmxqrbdhj"

# 发送邮件的地址和接收邮件的地址
sender = '642825572@qq.com'
receivers = ['jackielics@qq.com']

# msg = 'My test for Python sending Email ...'
msg = '''
<p> Python SMTP for HTML </p>
<p> <a herf = "https://www.baidu.com"> BAIDU </a> </p>
'''

# 创建一个文本类型的邮件，内容为“My test for Python sending Email ...”
# message = MIMEText(msg, 'plain', 'utf-8') # 内容，格式，编码
message = MIMEText(msg, 'html', 'utf-8') # 内容，格式，编码


message['From'] = Header("Python SMTP", 'utf-8') # 发送者名称
message['To'] = Header('Receivers', 'utf-8') # 接收者名称
message['Subject'] = Header('Python SMTP to receivers', 'utf-8') # 邮件主题

try:
    smtp_obj = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，SMTP_SSL是安全传输协议

    # # 登录SMTP服务器，需要先开启SMTP服务并获取授权码
    smtp_obj.login(user, code)

    # 发送邮件
    smtp_obj.sendmail(sender, receivers, message.as_string())

    # 打印发送成功信息
    print("Email is sending successfully!")
except Exception as e:
    # 打印发送失败信息
    print("Error is", e)

