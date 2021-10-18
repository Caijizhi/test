# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: test.py
# @Software: PyCharm
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'    #必须参数，android平台不区分大小写
desired_caps['platformVersion'] = '7.1.2'   #必须参数，定义被测手机的版本号（设置-关于本机-android版本，大版本不能错，小版本可以不写）
desired_caps['deviceName'] = '127.0.0.1:62001'  #可以写任意值，但不能不写
# app的信息
desired_caps['appPackage'] = 'com.sina.weibo'    #必须参数，指定被测软件包名
desired_caps['appActivity'] = '.SplashActivity'   #必须参数，指定打开的app的页面是哪个
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


# driver.find_element_by_id('com.sina.weibo:id/tv_for_psw_login').click()
# el1 = driver.find_element_by_id("com.sina.weibo:id/et_pws_username")
# el1.send_keys("13616081897")
# el2 = driver.find_element_by_id("com.sina.weibo:id/et_pwd")
# el2.send_keys("caijizhi666")
# el3 = driver.find_element_by_id("com.sina.weibo:id/bn_pws_Login")
# el3.click()
# data = driver.find_element_by_id('com.sina.weibo:id/tv_psw_tips').text


el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]")
el1.click()
time.sleep(2)
el2 = driver.find_element_by_id("com.sina.weibo:id/titleBackOuter")
el2.click()
time.sleep(3)
try:
    el3 = driver.find_element_by_id("com.sina.weibo:id/iv_psw")
    el3.click()
except Exception:
    el3 = driver.find_element_by_id("com.sina.weibo:id/tv_for_psw_login")
    el3.click()
finally:
    el4 = driver.find_element_by_id("com.sina.weibo:id/et_pws_username")
    el4.send_keys("13616081897")
    el5 = driver.find_element_by_id("com.sina.weibo:id/et_pwd")
    el5.send_keys("caijizhi666")
    try:
        el7 = driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol")
        el7.click()
    except:
        pass
    try:
        el8 = driver.find_element_by_id("com.sina.weibo:id/btn_login_view_psw")
        el8.click()
    except:
        el8 = driver.find_element_by_id("com.sina.weibo:id/bn_pws_Login")
        el8.click()
    time.sleep(10)
    print(driver.current_activity)
time.sleep(3)
