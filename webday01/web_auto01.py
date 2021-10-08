# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: web_auto01.py
# @Software: PyCharm
#京东查询
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = r'https://www.jd.com/'
driver.get(url)
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_c']").send_keys('电脑')
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('''//*[@id="J_goodsList"]/ul/li[7]/div/div[3]/a''').click()

driver.implicitly_wait(5)
dsa = driver.window_handles
driver.switch_to.window(dsa[1])

driver.implicitly_wait(30)
driver.quit()
