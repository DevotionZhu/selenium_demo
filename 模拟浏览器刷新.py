# -*- coding: utf-8 -*-
# @Time : 2020/3/21 23:04
# @Author : wangmengmeng
from selenium import webdriver

dr = webdriver.Chrome("D:/soft/chromedriver.exe")
dr.maximize_window()
dr.get('https://www.baidu.com')
dr.refresh()  # 模拟浏览器刷新
dr.quit()
