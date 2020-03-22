# -*- coding: utf-8 -*-
# @Time : 2020/3/22 13:19
# @Author : wangmengmeng
"""
webdriver只能在一个页面上对元素识别与定位，对于frame/iframe表单内嵌页面上的元素无法直接定位。
这时就需要通过switch_to.frame()方法将当前定位的主体切换为frame/iframe表单的内嵌页面中
"""
from selenium import webdriver

driver = webdriver.Chrome("D:/soft/chromedriver.exe")
driver.get("http://126.com/")
driver.maximize_window()
driver.find_element_by_css_selector('.u-login-entry').click()
dingwei = driver.find_element_by_css_selector('div#loginDiv>iframe')
driver.switch_to.frame(dingwei)  # switch_to.frame()默认可以直接获取表单的id或name属性。如果没有可用给的id和name属性，我们可以自行定位，再将定位对象传递给switch_to.frame()方法
# driver.switch_to.frame(0)
driver.find_element_by_css_selector('.j-nameforslide').send_keys('wmm_0165')  # 模拟键盘像输入框输入内容
driver.find_element_by_css_selector('input[name=email]').clear()  # 清楚文本输入得内容
driver.quit()