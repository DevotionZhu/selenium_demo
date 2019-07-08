# -*- coding: utf-8 -*-
# @Time : 2019/7/8 16:43
# @Author : wangmengmeng
from config.read_config import ReadConfig
from selenium import webdriver

rc = ReadConfig()
url = rc.get('auditcenter','login_url')
dr = webdriver.Chrome("D:/soft/49chrome/Chrome/chromedriver.exe")
dr.get(url)
dr.maximize_window()
test1 = dr.find_element_by_id('name')
test1.send_keys('wangmm')
test2 = dr.find_element_by_xpath('//input[@placeholder="请输入密码"]')    # 注意单引号内不能有引号
test2.send_keys('123456')
test3 = dr.find_element_by_xpath('//span[text()="登 录"]')  # 注意登与录之间有空格
test3.click()
# dr.close()