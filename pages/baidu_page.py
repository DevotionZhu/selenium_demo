# -*- coding: utf-8 -*-
# @Time : 2019/7/8 14:04
# @Author : wangmengmeng
from pages.base_page import BasePage


class baidu(BasePage):
    kw = ['id', 'kw']  # 定位搜索输入框
    su = ['id', 'su']  # 搜索按钮

    def kw_send(self,value):
        self.send_keys(self.kw,value)

    def su_click(self):
        self.click(self.su)



