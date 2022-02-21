#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2021/12/30 15:34
import os
from public.models.getdriver import browser
from selenium.webdriver.common.by import By
from public.page.basepage import BasePage
from public.models.getyaml import YamlRead
from config import setting

configdata = YamlRead(os.path.join(setting.TEST_Element_YAML, 'login.yaml'))


class TestLogin(BasePage):

    def login_google(self):
        pass

    switch_computerlogin_loc = (By.ID, configdata.get_elementinfo(0))

    def switch_to_computerlogin(self):
        '''
        切换登录模式：电脑登录
        :return:
        '''
        self.find_clickable_elem(mark=self.switch_computerlogin_loc).click()

    name_loc = (By.NAME, configdata.get_elementinfo(1))

    def send_keys_username(self, username):
        '''
        输入用户名
        :param username:
        :return:
        '''
        self.send_keys(self.name_loc, username)

    password_loc = (By.NAME, configdata.get_elementinfo(2))

    def send_keys_password(self, password):
        '''
        输入密码
        :return:
        '''
        self.send_keys(self.password_loc, password)

    button_loc = (By.ID, configdata.get_elementinfo(3))

    def click_button(self):
        '''
        点击登录按钮
        :return:
        '''
        self.click(self.button_loc)

    current_username_loc = (By.XPATH, configdata.get_checkelementinfo(2))

    def login_success(self):
        return self.find_presence_elem(self.current_username_loc).text

    login_username_empty_loc = (By.XPATH, configdata.get_checkelementinfo(0))

    def login_username_empty(self):
        '''用户名为空提示'''
        return self.find_presence_elem(self.login_username_empty_loc).text

    login_password_empty_loc = (By.XPATH, configdata.get_checkelementinfo(1))

    def login_password_empty(self):
        '''密码为空提示'''
        return self.find_presence_elem(self.login_password_empty_loc).text

    login_failure_loc = (By.XPATH, configdata.get_checkelementinfo(3))

    def login_failure(self):
        '''登录失败提示'''
        return self.find_presence_elem(self.login_failure_loc).text

    loginout_loc = (By.XPATH, configdata.get_checkelementinfo(4))

    def loginout(self):
        '''登出后信息'''
        return self.find_presence_elem(self.loginout_loc).text

    exit_loc = (By.XPATH, configdata.get_elementinfo(6))

    def login_exit(self):
        '''
        1.点击当前用户名弹出下拉弹框
        2.点击退出
        :return:
        '''
        self.find_clickable_elem(self.current_username_loc).click()
        self.find_clickable_elem(self.exit_loc).click()

    '''组合操作'''

    def test_login_user(self, username, password):
        '''
        账号密码登录
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        self.open()
        self.switch_to_computerlogin()
        self.send_keys_username(username)
        self.send_keys_password(password)
        self.click_button()


# if __name__ == '__main__':
#     from public.models.getdriver import browser
#     username = 'david.luo'
#     password = 'Ni&Li12345'
#     driver = browser()
#     case = TestLogin(driver)
#     case.test_login1_user(username, password)
    # case.login_exit()
    # a.switch_to_computerlogin
