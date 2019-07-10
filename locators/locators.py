# -*- coding: utf-8 -*-
# @Time : 2019/7/8 17:30
# @Author : wangmengmeng
from selenium.webdriver.common.by import By


class Locaors:
    # 元素定位器
    login_page_locators = {
        "username": (By.ID, "name"),
        "password": (By.XPATH, "//input[@placeholder='请输入密码']"),
        'login_button': (By.XPATH, "//span[text()='登 录']")
    }


if __name__ == '__main__':
    t = Locaors()
    print(t.login_page_locators["login_button"])
    # output: ('xpath', "//span[text()='登 录']")
