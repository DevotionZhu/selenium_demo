# -*- coding: utf-8 -*-
# @Time : 2019/7/9 10:26
# @Author : wangmengmeng
import  unittest
from pages.login_page import LoginPage
from selenium import webdriver
from config.read_config import ReadConfig
import time

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Chrome("D:/soft/49chrome/Chrome/chromedriver.exe")
        cls.cr = ReadConfig()
        cls.url = cls.cr.get('auditcenter','login_url')
        cls.login = LoginPage(cls.driver)
        cls.login.open(cls.url)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver = cls.driver.quit()

    def test_01(self):
        time.sleep(6)
        self.driver.implicitly_wait(30)
        self.login.input_username('wangmm')
        self.login.input_password("123456")
        self.login.login()

if __name__ == '__main__':
    unittest.main()