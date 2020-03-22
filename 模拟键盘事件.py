# -*- coding: utf-8 -*-
# @Time : 2020/3/22 13:33
# @Author : wangmengmeng
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

dr = webdriver.Chrome("D:/soft/chromedriver.exe")
dr.maximize_window()
dr.get('https://www.baidu.com')

dr.find_element_by_css_selector('input[name=wd]').send_keys('seleniumm')  # 输入框输入内容
dr.find_element_by_css_selector('input[name=wd]').send_keys(Keys.BACK_SPACE)  # 删除多输入的一个m

time.sleep(2)
dr.find_element_by_id('su').send_keys(Keys.ENTER)  # 通过回车键来代替单击操作

dr.quit()
