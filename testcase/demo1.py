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

import setting
from getyaml import YamlRead

# testdata = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'testdata_marketchannel.yaml')).yaml_all()
# print(testdata)

testdata_add = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'testdata_add_marketchannel.yaml')).yaml_all()
print(testdata_add)
print(int(time.time()))