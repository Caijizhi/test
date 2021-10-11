# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: HKR.py
# @Software: PyCharm
from selenium import webdriver
import time

url = r'http://localhost:8080/HKR/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath('''/html/body/div/div/div[1]/div[2]/a[2]''').click()
driver.find_element_by_xpath('''//*[@id="loginname"]''').send_keys('jason')
driver.find_element_by_xpath('''//*[@id="password"]''').send_keys('admin')
driver.find_element_by_xpath('''//*[@id="submit"]''').click()
time.sleep(2)
#教室管理:查询
driver.find_element_by_xpath('''//*[@id="_easyui_tree_11"]''').click()
time.sleep(1)
#driver.find_element_by_xpath('''//*[@id="tt"]/div[2]/div[2]''').click()
driver.find_element_by_xpath('''//*[@id="sear_teaname"]''').send_keys('曹')
driver.find_element_by_xpath('''//*[@id="search_user"]''').click()

#重置密码
driver.find_element_by_xpath('''//*[@id="datagrid-row-r1-2-0"]/td[9]/div/a''').click()
alert1 = driver.switch_to.alert
alert1.accept()
#学生模块
driver.find_element_by_xpath('''//*[@id="_easyui_tree_12"]''').click()
time.sleep(1)

driver.find_element_by_xpath('''//*[@id="J-stu"]''').send_keys('肖')
driver.find_element_by_xpath('''//*[@id="stu_panel"]/div/div/div[1]/table/tbody/tr/td[4]''').click()    #搜索

time.sleep(1)
driver.find_element_by_xpath('''//*[@id="datagrid-row-r2-2-0"]/td[11]''').click()     #设置毕业
time.sleep(1)
driver.find_element_by_xpath('''/html/body/div[9]/div[3]/a''').click()    #确定
time.sleep(2)
driver.find_element_by_xpath('''//*[@id="tt"]/div[1]/div[3]/ul/li[3]/a[2]''').click()
time.sleep(1)
driver.find_element_by_xpath('''//*[@id="_easyui_tree_12"]''').click()
time.sleep(1)
driver.find_element_by_xpath('''//*[@id="tt"]/div[1]/div[3]/ul/li[3]/a[1]/span[1]''').click()

driver.find_element_by_xpath('''//*[@id="J-phone"]''').send_keys('''13548554150''')
time.sleep(1)
driver.find_element_by_xpath('''//*[@id="stu_panel"]/div/div/div[1]/table/tbody/tr/td[4]''').click()
time.sleep(1)
driver.find_element_by_xpath('''//*[@id="stu_panel"]/div/div''').click()    #不知道为什么切换
time.sleep(1)
driver.find_element_by_xpath('''//*[@id="datagrid-row-r3-2-0"]/td[11]''').click() #设置未毕业
time.sleep(1)
driver.find_element_by_xpath('''/html/body/div[9]/div[3]/a''').click()

#课程管理
driver.find_element_by_xpath('''//*[@id="_easyui_tree_13"]''').click()
time.sleep(1)

time.sleep(1)
driver.find_element_by_xpath('''//*[@id="course_panel"]/div/div/div[1]/table/tbody/tr/td/a''').click()
driver.find_element_by_xpath('''//*[@id="course_form_add"]/table/tbody/tr[1]/td[2]/input''').send_keys('逻辑课')
driver.find_element_by_xpath('''//*[@id="course_form_add"]/table/tbody/tr[2]/td[2]/textarea''').send_keys('脑筋急转弯')
time.sleep(1)
#driver.find_element_by_xpath('''/html/body/div[7]/div[3]/a[2]/span''').click()
driver.find_element_by_xpath('''/html/body/div[9]/div[3]/a[1]/span''').click()  #添加



time.sleep(2)
driver.quit()
