# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: LoginOper.py
# @Software: PyCharm
import time
class LoginOper:
    def __init__(self,driver):
        self.driver = driver
    def login(self,username,password):
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]")
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element_by_id("com.sina.weibo:id/titleBackOuter")
        el2.click()
        time.sleep(3)
        try:
            el3 = self.driver.find_element_by_id("com.sina.weibo:id/iv_psw")
            el3.click()
        except Exception:
            el3 = self.driver.find_element_by_id("com.sina.weibo:id/tv_for_psw_login")
            el3.click()
        finally:
            try:
                el4 = self.driver.find_element_by_id("com.sina.weibo:id/et_pws_username")
                el4.send_keys(username)
            except Exception:
                el4 = self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_uname")
                el4.send_keys(username)
            try:
                el5 = self.driver.find_element_by_id("com.sina.weibo:id/et_pwd")
                el5.send_keys(password)
            except Exception:
                el5 = self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_psw")
                el5.send_keys(password)
            try:
                el7 = self.driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol")
                el7.click()
            except Exception:
                pass
            try:
                el8 = self.driver.find_element_by_id("com.sina.weibo:id/btn_login_view_psw")
                el8.click()
            except Exception:
                el8 = self.driver.find_element_by_id("com.sina.weibo:id/bn_pws_Login")
                el8.click()
            try:
                time.sleep(5)
                self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]").click()
            except Exception:
                pass
    def get_error_data(self):
        return self.driver.current_activity
    def get_success_data(self):
        return self.driver.current_activity


