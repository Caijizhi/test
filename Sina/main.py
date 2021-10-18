# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: main.py
# @Software: PyCharm
import HTMLTestRunner
import unittest
import os
import threading

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Test*.py")
print(tests)
runner = HTMLTestRunner.HTMLTestRunner(
    title="Sina微博登录测试",
    description="Sina微博测试",
    verbosity=1,
    stream=open(file="SinaLogin.html", mode="wb")
)
runner.run(tests)