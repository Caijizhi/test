# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: TestLogin.py
# @Software: PyCharm
from unittest import TestCase
from appium import webdriver
from ddt import ddt
from ddt import data
# from ddt import unpack
from datasource import datasource
from LoginOper import LoginOper  # 页面的操作逻辑
import time
import threading


@ddt
class TestLogin(TestCase):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'  # 必须参数，android平台不区分大小写
    desired_caps['platformVersion'] = '7.1.2'  # 必须参数，定义被测手机的版本号（设置-关于本机-android版本，大版本不能错，小版本可以不写）
    desired_caps['deviceName'] = '127.0.0.1:62001'  # 可以写任意值，但不能不写
    # app的信息
    desired_caps['appPackage'] = 'com.sina.weibo'  # 必须参数，指定被测软件包名
    desired_caps['appActivity'] = '.SplashActivity'  # 必须参数，指定打开的app的页面是哪个
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    def setUp(self) -> None:
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        time.sleep(5)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()  # 退出app

        # 登陆成功用例

    @data(*datasource.login_success_data)
    def testLoginsuccess(self, testdata):
        # 提取用户名，密码，期望结果
        username = testdata["username"]
        password = testdata["password"]
        print(password)
        expect = testdata["expect"]

        login = LoginOper(self.driver)
        login.login(username, password)
        time.sleep(3)
        #  获取实际结果
        result = login.get_success_data()
        print(result)
        time.sleep(1)
        # 断言
        self.assertEqual(expect, result)

    # 登录失败的用例
    @data(*datasource.login_error_data)
    def testLoginerror(self, testdata):
        # 提取用户名，密码，期望结果
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = LoginOper(self.driver)
        login.login(username, password)
        time.sleep(3)
        # 获取实际结果
        result = login.get_error_data()
        time.sleep(1)
        print(result)
        # 断言
        self.assertEqual(expect, result)
# if __name__ == '__main__':
#     th1 = threading.Thread(target=TestLogin.testLoginsuccess)  # 创建线程
#     th2 = threading.Thread(target=TestLogin.testLoginerror)
#     # th1.setDaemon(True)   #线程守护
#     # th2.setDaemon(True)
#     th1.start()  # 启动线程
#     th2.start()
