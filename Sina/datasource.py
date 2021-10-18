# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: datasource.py
# @Software: PyCharm
class datasource:
    #成功的用例
    login_success_data = [
        {"username":'13616081897','password':'caijizhi666','expect':'.MainTabActivity'}
    ]
    #失败的用例
    login_error_data = [
        {"username": '13616081897', 'password': 'caijadssadas', 'expect': '.account.login.LoginActivity'}
    ]




















