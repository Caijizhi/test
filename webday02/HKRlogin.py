# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: HKRlogin.py
# @Software: PyCharm
from selenium import webdriver
import time

url = r'http://localhost:8080/HKR/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.find_element_by_partial_link_text('新来的童鞋').click()
driver.find_element_by_xpath('''//*[@id="loginname"]''').send_keys('caijizhi')
driver.find_element_by_xpath('''//*[@id="msform"]/fieldset[1]/input[2]''').send_keys('caijizhi')
driver.find_element_by_xpath('''//*[@id="pwd"]''').send_keys('123456')
driver.find_element_by_xpath('''//*[@id="msform"]/fieldset[1]/input[4]''').send_keys('123456')
time.sleep(1)
driver.find_element_by_xpath('''//*[@id="msform"]/fieldset[1]/input[5]''').click()
time.sleep(1)
driver.find_element_by_xpath('''//*[@id="valid_age"]''').send_keys('20')
time.sleep(1)
driver.find_element_by_xpath('''//*[@id="msform"]/fieldset[2]/input[3]''').click()

driver.find_element_by_xpath('''//*[@id="reg_mail"]''').send_keys('576579281@qq.com')
driver.find_element_by_xpath('''//*[@id="reg_phone"]''').send_keys('13635555555')
driver.find_element_by_xpath('''//*[@id="msform"]/fieldset[3]/textarea''').send_keys('home')
time.sleep(1)
driver.find_element_by_xpath('''//*[@id="btn_reg"]''').click()


