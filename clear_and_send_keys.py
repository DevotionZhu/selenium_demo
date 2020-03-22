# -*- coding: utf-8 -*-
# @Time : 2020/3/21 23:14
# @Author : wangmengmeng
from selenium import webdriver

driver = webdriver.Chrome("D:/soft/chromedriver.exe")
driver.get("http://126.com/")
driver.maximize_window()
driver.find_element_by_css_selector('.u-login-entry').click()
driver.switch_to.frame(0)
driver.find_element_by_css_selector('.j-nameforslide').send_keys('wmm_0165')  # 模拟键盘像输入框输入内容
driver.find_element_by_css_selector('input[name=email]').clear()  # 清楚文本输入得内容
driver.quit()
