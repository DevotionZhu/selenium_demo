# -*- coding: utf-8 -*-
# @Time : 2020/3/22 0:53
# @Author : wangmengmeng
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dr = webdriver.Chrome("D:/soft/chromedriver.exe")
dr.maximize_window()
dr.get('https://www.baidu.com')
element = WebDriverWait(dr, 5, 0.5).until(EC.presence_of_element_located(("css selector", 'input[name=wd]')))  # ignored_exceptions=None
dr.quit()
