# -*- coding: utf-8 -*-
# @Time : 2019/7/7 23:18
# @Author : wangmengmeng

from selenium import webdriver
import time
dr = webdriver.Chrome("D:/soft/49chrome/Chrome/chromedriver.exe")  # 初始化chrome浏览器实例
dr.maximize_window()  # 浏览器最大化
dr.get('https://www.baidu.com')  # 打开百度首页
time.sleep(15)
test = dr.find_element_by_name('wd')#通过name属性定位输入框
test.send_keys('测试一下')#输入测试一下
