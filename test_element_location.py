# -*- coding: utf-8 -*-
# @Time : 2019/7/8 16:01
# @Author : wangmengmeng
import unittest
from selenium import webdriver



class TestLocate(unittest.TestCase):

    def test_01(self):
        # 使用name定位
        dr = webdriver.Chrome("D:/soft/49chrome/Chrome/chromedriver.exe")
        dr.maximize_window()
        dr.get('https://www.baidu.com')
        test = dr.find_element_by_name('wd')
        test.send_keys('测试输入框')
        dr.close()

    def test_02(self):
        # 使用id定位
        dr = webdriver.Chrome("D:/soft/49chrome/Chrome/chromedriver.exe")
        dr.maximize_window()
        dr.get('https://www.baidu.com')
        test = dr.find_element_by_id('kw')
        test.send_keys('测试一下')
        dr.close()

    def test_03(self):
        # 使用class定位
        dr = webdriver.Chrome("D:/soft/49chrome/Chrome/chromedriver.exe")
        dr.maximize_window()
        dr.get('https://www.baidu.com')
        test = dr.find_element_by_class_name('s_ipt')
        test.send_keys('测试一下')
        dr.close()



# xpath元素定位




if __name__ == '__main__':
    unittest.main()