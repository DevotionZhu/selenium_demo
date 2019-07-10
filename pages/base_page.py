# -*- coding: utf-8 -*-
# @Time : 2019/7/7 22:25
# @Author : wangmengmeng
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, *locator):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
            return element  # 返回页面元素的位置对象 # 类型是<class 'selenium.webdriver.remote.webelement.WebElement'>
        except NoSuchElementException:
            print("%s 页面中未能找到 %s 元素" % (self, locator))

    def send_keys(self, locator, value, clear_first=False):
        """封装send_keys()方法"""
        try:
            # locator = getattr(self, "_%s"% locator)
            if clear_first:
                self.find_element(*locator).clear()  # 判断是否需要清除输入框信息
            self.find_element(*locator).send_keys(value)
        except AttributeError:
            print("%s 页面中未找到 %s 元素" % (self, locator))

    def click(self, locator):
        """封装click()方法"""
        self.find_element(*locator).click()


if __name__ == '__main__':
    dr = webdriver.Chrome("D:/soft/49chrome/Chrome/chromedriver.exe")
    bp = BasePage(dr)
    dr.maximize_window()
    dr.get('https://www.baidu.com')
    time.sleep(5)
    elemn= ['id', "kw"]
    bp.send_keys(elemn,"测试一下")
    bp.click(['id','su'])



