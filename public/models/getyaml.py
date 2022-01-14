#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2021/12/30 15:34
import os

import yaml
from public.models.logger import Logs

# 1.在打开文件之前判断文件是否存在，将判断写在初始化方法内
class YamlRead():
    def __init__(self, filepath):
        # 实例化封装的日志模块
        self.logs = Logs()
        # 判断添加
        if os.path.exists(filepath):
            self.yamlpath = filepath
        else:
            raise FileNotFoundError('文件不存在')
        # 在初始化的最后加上一个默认参数，用于判断文件是否已经被读取
        self.all_data = None

    # 判断文件是否存在后尝试读取数据（做判断防止重复读取）
    def yaml_all(self):
        # 判断文件是否已经被读取
        if not self.all_data:
            # 读取文件
            with open(self.yamlpath, 'r', encoding="utf-8") as f:
                # 获取文件中所有的值
                file_data = f.read()
            self.all_data = yaml.load(file_data, Loader=yaml.FullLoader)
        return self.all_data

    # 通过索引值获取yaml文件中testdata的elementinfo字段
    def get_elementinfo(self, i):
        if i in range(0, len(self.yaml_all()['testcase'])):
            return self.yaml_all()['testcase'][i]['element_info']
        else:
            self.logs.info('索引值超出取值范围，无法获取testdata--->elementinfo')

    # 通过索引值获取yaml文件中check的elementinfo字段
    def get_checkelementinfo(self, i):
        if i in range(0, len(self.yaml_all()['check'])):
            return self.yaml_all()['check'][i]['element_info']
        else:
            self.logs.info('索引值超出取值范围，无法获取check--->elementinfo')

    def get_yamlturple(self):
        with open(self.yamlpath, 'r', encoding="utf-8") as f:
            file_data = f.read()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data


# projectpath=os.path.abspath(os.path.join(os.getcwd(),'../..'))
# filepath=projectpath+os.sep+'config'+os.sep+'login.yaml'
# print(filepath)
# print(os.path.abspath(os.path.dirname(os.getcwd())))
#
# print(os.path.abspath(os.path.join(os.getcwd(),'../..')))
if __name__ == '__main__':
    a = YamlRead('C:/Users/Administrator/PycharmProjects/pytest_demo/testyaml/login.yaml')
    # print(a.yaml_all())
    # print(a.yaml_all()[0]['testcase'][0]['element_info'])
    # print(a.yaml_all())
    # for i in range(0, len(a.yaml_all()[0]['testcase'])):
    #     print(i, a.yaml_all()[0]['testcase'][i])
    # print(a.get_checkelementinfo(0))
    # print(a.get_checkelementinfo(2))
    print(a.yaml_all())
    print(a.get_elementinfo(1))
    print(a.get_checkelementinfo(1))

