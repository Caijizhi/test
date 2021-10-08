# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: web_auto02.py
# @Software: PyCharm

from selenium import webdriver
import time
#百度查询
url = 'https://www.baidu.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
driver.find_element_by_xpath('''//*[@id="kw"]''').send_keys('王者荣耀')
driver.find_element_by_xpath('''//*[@id="su"]''').click()
# driver.find_element_by_xpath('''//*[@id="3001"]/div/div[1]/div/div/h3/div/a[1]''').click()
time.sleep(5)
driver.quit()


