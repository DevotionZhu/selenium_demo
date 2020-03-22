# -*- coding: utf-8 -*-
# @Time : 2020/3/22 11:57
# @Author : wangmengmeng
"""
在页面操作过程中有时候点击某个链接会弹出新的窗口，这时就需要主机切换到新打开的窗口上进行操作
"""
from selenium import webdriver
import time

dr = webdriver.Chrome("D:/soft/chromedriver.exe")
dr.maximize_window()
dr.get('https://www.baidu.com')
search_windows = dr.current_window_handle  # 获取当前窗口句柄
dr.find_element_by_css_selector('div#u1>a[name=tj_login]').click()  # 点击登录
time.sleep(2)
dr.find_element_by_css_selector('.tang-pass-footerBarPhoenix+a').click()  # 点击立即注册

all_handles = dr.window_handles  # 获取当前所有打开的窗口的句柄

# 进入注册窗口
for handle in all_handles:
    if handle != search_windows:
        dr.switch_to.window(handle)  # 切换到相应的窗口
        print('now register window!')
        time.sleep(2)

# 回到搜索窗口
for handle in all_handles:
    if handle == search_windows:
        dr.switch_to.window(handle)
        print('now search window!')
        time.sleep(2)

dr.quit()
