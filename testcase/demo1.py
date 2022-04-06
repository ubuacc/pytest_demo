#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/2/10 15:00

# import copy
#
# class MobilePhone:
#     def __init__(self,cpu,screen):
#         self.cpu = cpu
#         self.screen = screen
#
#
# class Cpu:
#     def calulate(self):
#         print("计算，算个12345")
#         print("cpu对象：",self)
#
#
# class Screen:
#     def show(self):
#         print("显示一个好看的画面，亮瞎你的钛合金大眼")
#         print("屏幕对象：",self)
#
# c = Cpu()
# s = Screen()
# m = MobilePhone(c,s)
#
# m.cpu.calulate()
#
# n = m
# print(m,n)
# print(id(m),id(n))
#
# m2 = copy.copy(m)
# print(m,m2)
# print(id(m),id(m2))
#
# m.cpu.calulate()
# m2.cpu.calulate()
#
# m3 = copy.deepcopy(m)
# print(m,m3)
# print(id(m),id(m3))
# m3.cpu.calulate()
import os
import time

from ruamel import yaml
from selenium.webdriver.common.by import By

import setting
from getyaml import YamlRead

# testdata = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'marketchannel.yaml')).yaml_all()
# print(testdata)

# testdata_add = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'add_marketchannel.yaml')).yaml_all()
# print(testdata_add)
# print(int(time.time()))
from page import basepage
from models import getdriver
from page.mdp_ipc_group import MarketGroup
import logger
from page.mdp_login import Login

# driver = getdriver.browser()
# log = logger.Logs()
# username = 'david.luo'
# password = 'Ni&Li12345'
# case = Login(driver)
# case.login_user(username, password)
# MarketGroup(driver).open_marketgroup()
# MarketGroup(driver).add_marketgroup('cn','test346','test','123','test')
# add_success = (By.XPATH, '/html/body/div[6]/span/div/div/div/span')
# while True:
#     a = basepage.BasePage(driver).find_presence_elem(add_success).text
#     if a is True:
#         print(a)
#         break
# print('jieshu')
# yaml = YAML()
from public.page.basepage import DataAssociation
da = DataAssociation()
def ac():
    testdata_add = 0
# print(testdata_add)
    setattr(da, 'data', testdata_add)
# print(getattr(da, 'data'))
# print('1')
# testdata_add[1]['data']['number'] = 'tes'
# print(testdata_add)
# with open(os.path.join(setting.TEST_DATA_YAML, 'marketgroup_process.yaml'), 'w', encoding='utf-8') as f:
#     yaml.round_trip_dump(testdata_add, f)
