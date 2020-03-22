# -*- coding: utf-8 -*-
# @Time : 2020/3/22 0:37
# @Author : wangmengmeng
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Chrome("D:/soft/chromedriver.exe")
dr.maximize_window()
dr.get('https://www.baidu.com')
shurukuang = dr.find_element_by_css_selector('input[name=wd]')
ActionChains(dr).context_click(shurukuang).perform()  # 鼠标右击
ActionChains(dr).move_to_element(shurukuang).perform()  # 鼠标悬停
ActionChains(dr).double_click(shurukuang).perform()  # 鼠标双击
# ActionChains(dr).drag_and_drop(source,target).perform()  # 鼠标拖放