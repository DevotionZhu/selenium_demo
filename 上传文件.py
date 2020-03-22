# -*- coding: utf-8 -*-
# @Time : 2020/3/22 13:43
# @Author : wangmengmeng
from selenium import webdriver
import time


driver = webdriver.Chrome("D:/soft/chromedriver.exe")
driver.get("https://pan.baidu.com/")
driver.maximize_window()
driver.find_element_by_css_selector(".tang-pass-footerBarULogin").click()  # 点击账号密码登录
driver.find_element_by_css_selector("#TANGRAM__PSP_4__userName").send_keys("15858183745") # 输入用户名
driver.find_element_by_css_selector("#TANGRAM__PSP_4__password").send_keys("Ww2548558583") # 输入密码
driver.find_element_by_css_selector(".pass-button-submit").click() # 点击登录
time.sleep(3)
driver.quit()

