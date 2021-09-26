# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: SendMessage.py
# @Software: PyCharm
import smtplib
import email
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import traceback
from email.mime.multipart import MIMEMultipart
from email.header import Header

class SendEmail:
    def __init__(self,sender,passwd,senderName,subject,reciver,smtpserver = 'smtp.qq.com'):
        '''

        :param sender: 发件人邮箱
        :param passwd: 发件人密码
        :param senderName: 发件人姓名
        :param subject: 主题
        :param reciver: 接受者邮箱
        :param smtpserver: 服务器
        '''
        self.sender = sender
        self.passwd = passwd
        self.senderName = senderName
        self.subject = subject
        self.reciver = reciver
        self.smtpserver = smtpserver
        #创建smtp对象
        self.smtp = smtplib.SMTP()
        self.smtp.connect(self.smtpserver,25)
    def __emailHeader(self):
        '''
        邮件标头
        :return:邮件对象
        '''
        message = MIMEMultipart()
        message['From'] = Header(self.senderName,'utf-8')
        message['To'] = ';'.join(self.reciver)
        message['Subject'] = Header(self.subject,'utf-8')
        return message
    def __connect(self,message):

        try:
            self.smtp.login(self.sender,self.passwd)
            self.smtp.sendmail(self.sender,self.reciver,message.as_string())
            self.smtp.quit()
        except Exception:
            traceback.print_exc()
            print('邮件失败')
        else:
            print('发送邮件成功')
    def sendAttachment(self,text,*attachPath):
        textPlain = MIMEText(text,'plain','utf-8')
        message = self.__emailHeader()
        message.attach(textPlain)
        for attach in attachPath:
            if not os.path.exists(attach):
                print('{0}附件路径不存在'.format(attach))
                return
            attachment = MIMEApplication(open(attach,'rb').read())
            attachment.add_header('Content-Disposition','attachment',filename = os.path.basename(attach))
            message.attach(attachment)
        self.__connect(message)


# s = SendEmail(sender='576579281@qq.com',passwd='marsahmlukgibebb',senderName='caijizhi',subject='test',reciver='1342493938@qq.com')
# s.sendAttachment('测试报告',r'C:\Users\caijizhi\PycharmProjects\SMS\Testwork\测试报告.html')
#

