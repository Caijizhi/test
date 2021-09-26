# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: main.py
# @Software: PyCharm
'''
    报告：
        1. 加载器：加载所有测试用例并得到所有用例
        2. 使用运行期运行这些测试用例并生成报告


'''
import HTMLTestRunner
import unittest
from SendMessage import SendEmail
import os

send = '576579281@qq.com'
sendname = 'caijizhi'
reciver = '1347394976@qq.com'

subject = '测试报告'
pwd = 'marsahmlukgibebb'
s = SendEmail(sender=send,senderName=sendname,passwd=pwd,subject=subject,reciver=reciver)
filename = '全部的测试报告.html'

test = unittest.defaultTestLoader.discover(r'C:\Users\caijizhi\PycharmProjects\SMS\Testwork',pattern='test.py')
runner = HTMLTestRunner.HTMLTestRunner(

    title = '这是计算器的测试报告',
    description = '这计算器的测试报告',
    verbosity = 1,
    stream = open(filename,mode='wb')
)
runner.run(test)



text = '这是全部的测试报告'
s.sendAttachment(text,os.path.realpath(filename))




