# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: suningTest.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('https://www.suning.com/')
driver.maximize_window()
driver.find_element_by_xpath('''//*[@id="searchKeywords"]''').send_keys('电脑')
driver.find_element_by_xpath('''//*[@id="searchSubmit"]''').click()
driver.find_element_by_xpath('''//*[@id="0070640451-11930949107"]/div''').click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
driver.find_element_by_xpath('''//*[@id="addCart"]''').click()
time.sleep(5)
driver.find_element_by_xpath('''/html/body/div[38]/div/div[2]/div/div[1]/a''').click()
driver.find_element_by_xpath('''//*[@id="cart-wrapper"]/div[3]/div/div/div[2]/div[2]/a''').click()
time.sleep(3)
driver.switch_to.frame('iframeLogin')
action = ActionChains(driver)
driver.find_element_by_xpath('''//*[@id="userName"]''').send_keys('13616081897')
driver.find_element_by_xpath('''//*[@id="password"]''').send_keys('13635208872ba')
driver.find_element_by_xpath('''//*[@id="submit"]''').click()
time.sleep(1)

slider = driver.find_element_by_xpath('''//*[@id="siller1_dt_child_content_containor"]/div[3]''')
#action.drag_and_drop_by_offset(slider,292,0)
# time.sleep(3)
action.click_and_hold(slider).move_by_offset(300,0).perform()
time.sleep(1)
action.release()
driver.find_element_by_xpath('''//*[@id="submit"]''').click()
