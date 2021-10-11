# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: web_auto01.py
# @Software: PyCharm
#京东查询
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


import time


driver = webdriver.Chrome()
action = ActionChains(driver)
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
driver.find_element_by_partial_link_text('加入购物车').click()
driver.find_element_by_xpath('''//*[@id="content"]/div[2]/div[1]/div/div[3]/a''').click()
driver.find_element_by_xpath('''//*[@id="loginname"]''').send_keys('小菜鸡cai')
driver.find_element_by_xpath('''//*[@id="nloginpwd"]''').send_keys('13635208872ba')
driver.find_element_by_xpath('''//*[@id="formlogin"]/div[5]/div''').click()
slider = driver.find_element_by_xpath('''//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]''')
lisy1 = [117,134,149,136,112,152,158,108]
while True:
    for i in lisy1:
        action.click_and_hold(slider).move_by_offset(i,0).perform()
        action.release()
