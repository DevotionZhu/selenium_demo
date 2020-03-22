# -*- coding: utf-8 -*-
# @Time : 2020/3/21 23:46
# @Author : wangmengmeng
from selenium import webdriver

dr = webdriver.Chrome("D:/soft/chromedriver.exe")
dr.maximize_window()
dr.get('https://www.baidu.com')

size = dr.find_element_by_css_selector('input[name=wd]').size  # 获取输入框的尺寸
print(size)
text = dr.find_element_by_css_selector('p:nth-of-type(5)>a').text
print(text)
type = dr.find_element_by_css_selector('input[id=su]').get_attribute('type')  # 获取元素的属性值
print(type)
result = dr.find_element_by_css_selector('input[id=su]').is_displayed()  # 元素结果是否可见,返回False或True
print(result)
