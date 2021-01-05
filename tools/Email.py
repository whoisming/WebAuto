# -*- coding: utf-8 -*-
# author:liucong

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tools import Config
from tools.log import get_logger


logger = get_logger('Email')


class Email(object):
    def __init__(self):
        self.smtp_server = Config.get_email_config("mail_host")
        self.username = Config.get_email_config("mail_user")
        self.password = Config.get_email_config("mail_pass")
        self.sender = Config.get_email_config("sender")
        # receivers为列表
        self.receivers = Config.get_email_config("receivers").split(',')
        self.addr_from = Config.get_email_config("from")
        self.addr_to = Config.get_email_config("to")

    # 设置邮件正文
    def set_content(self):
        send_time = time.strftime('%Y-%m-%d %H:%M:%S')
        msg = MIMEText("{}的测试报告结果".format(send_time), 'plain', 'utf-8')  # 邮件正文
        msg['From'] = self.addr_from  # 发送邮件的地址
        msg['To'] = self.addr_to  # 接收邮件的地址
        subject = "{} Web自动化测试报告".format(send_time)  # 邮件标题
        msg['Subject'] = subject
        return msg

    def send_email(self):
        # 第三方 SMTP 服务
        server = smtplib.SMTP(self.smtp_server, 25)
        server.login(self.username, self.password)
        msg = self.set_content()
        logger.info('----------------------------> 邮件发送中')
        server.sendmail(self.sender, self.receivers, msg.as_string())
        logger.info('----------------------------> 邮件发送成功')
        server.quit()
