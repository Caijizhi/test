import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="HKR登陆测试",
    description="HKR登陆详细测试【成功，失败】",
    verbosity=1,
    stream=open(file="HKR测试报告.html", mode="wb")
)
runner.run(tests)
