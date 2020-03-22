# -*- coding: utf-8 -*-
# @Time : 2020/3/21 22:43
# @Author : wangmengmeng
from selenium import webdriver


driver = webdriver.Chrome("D:/soft/chromedriver.exe")
first_url = 'https://www.baidu.com/'
print("now access %s"%first_url)
driver.get(first_url)

second_url = 'http://news.baidu.com/'
print("now access %s"%second_url)
driver.get(second_url)

print("back to %s"%first_url)
driver.back()

print("forward to %s"%second_url)
driver.forward()

driver.quit()