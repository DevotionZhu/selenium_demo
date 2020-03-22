# -*- coding: utf-8 -*-
# @Time : 2020/3/22 0:47
# @Author : wangmengmeng
from selenium import webdriver
dr = webdriver.Chrome("D:/soft/chromedriver.exe")
dr.maximize_window()
dr.get('https://www.baidu.com')
print(dr.title)  # 获取当前页面标题
print(dr.current_url)  # 获取当前页面url
dr.quit()