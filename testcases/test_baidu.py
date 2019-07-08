# -*- coding: utf-8 -*-
# @Time : 2019/7/8 15:00
# @Author : wangmengmeng
from selenium import webdriver
from pages.baidu_page import baidu
import unittest

class BaiDu(unittest.TestCase):
    def test_baidu(self):
        dr = webdriver.Chrome("D:/soft/49chrome/Chrome/chromedriver.exe")
        dr.get('https://www.baidu.com')
        dr.maximize_window()
        bai = baidu(dr)
        bai.kw_send('selenium')
        bai.su_click()

if __name__ == '__main__':
    unittest.main()