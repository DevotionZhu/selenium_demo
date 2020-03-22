# -*- coding: utf-8 -*-
# @Time : 2019/7/8 16:02
# @Author : wangmengmeng


from selenium import webdriver

dr = webdriver.Chrome("D:/soft/chromedriver.exe")
dr.maximize_window()
dr.get('https://www.baidu.com')
dr.close()
