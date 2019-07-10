# -*- coding: utf-8 -*-
# @Time : 2019/7/8 17:18
# @Author : wangmengmeng
from pages.base_page import BasePage
from locators.locators import Locaors


class LoginPage(BasePage):
    username = Locaors.login_page_locators['username']
    password  = Locaors.login_page_locators['password']
    login_button = Locaors.login_page_locators['login_button']


    def input_username(self,value):
        self.send_keys(self.username,value)

    def input_password(self,value):
        self.send_keys(self.password,value)

    def login(self):
        self.click(self.login_button)
