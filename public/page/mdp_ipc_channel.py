#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/2/17 15:44

import os
from time import sleep

from selenium.webdriver.common.by import By
from public.page.basepage import BasePage, DataAssociation
DA = DataAssociation()
from public.models.getyaml import YamlRead
from config import setting


configdata = YamlRead(os.path.join(setting.TEST_Element_YAML, 'ipc_marketchannel.yaml'))


class MarketChannel(BasePage):

    ipc_select_loc = (By.XPATH, configdata.get_elementinfo(0))
    def click_ipc_select(self):
        """
        点击IPC主数据下拉框
        :return:
        """
        self.find_clickable_elem(self.ipc_select_loc).click()

    channel_loc = (By.XPATH, configdata.get_elementinfo(1))
    def click_channel(self):
        """
        点击市场大区进入市场大区页面
        :return:
        """
        self.find_clickable_elem(self.channel_loc).click()

    number_loc = (By.XPATH, configdata.get_elementinfo(2))
    def number(self, number):
        """
        输入市场大区编号
        :param number:
        :return:
        """
        self.send_keys(self.number_loc, number)

    abbr_name_loc = (By.XPATH, configdata.get_elementinfo(3))
    def abbr_name(self, abbr_name):
        """
        输入缩写
        :param abbr_name:
        :return:
        """
        self.send_keys(self.abbr_name_loc, abbr_name)

    click_search_button_loc = (By.XPATH, configdata.get_elementinfo(4))
    def click_search_button(self):
        """
        点击查询按钮
        :return:
        """
        self.click(self.click_search_button_loc)

    click_add_button_loc = (By.XPATH, configdata.get_elementinfo(5))
    def click_add_button(self):
        """
        点击添加按钮
        :return:
        """
        self.click(self.click_add_button_loc)

    add_abbr_name_loc = (By.XPATH, configdata.get_elementinfo(6))
    def add_abbr_name(self, add_abbr_name):
        """
        新增页面输入缩写
        :param add_abbr_name:
        :return:
        """
        self.send_keys(self.add_abbr_name_loc, add_abbr_name)

    add_cn_name_loc = (By.XPATH, configdata.get_elementinfo(7))
    def add_cn_name(self, add_cn_name):
        """
        新增页面输入中文名
        :return:
        """
        self.send_keys(self.add_cn_name_loc, add_cn_name)

    add_en_name_loc = (By.XPATH, configdata.get_elementinfo(8))
    def add_en_name(self,add_en_name):
        """
        新增页面输入英文名
        :param add_en_name:
        :return:
        """
        self.send_keys(self.add_en_name_loc, add_en_name)

    add_remark_loc = (By.XPATH, configdata.get_elementinfo(9))
    def add_remark(self, add_remark):
        """
        新增页面输入备注
        :return:
        """
        self.send_keys(self.add_remark_loc,add_remark)

    add_enable_loc = (By.XPATH, configdata.get_elementinfo(10))
    def add_enable(self):
        """
        新增页面启用状态
        :return:
        """
        self.click(self.add_enable_loc)

    add_disabled_loc = (By.XPATH, configdata.get_elementinfo(11))
    def add_disabled(self):
        """
        新增页面禁用状态
        :return:
        """
        self.click(self.add_disabled_loc)

    add_save_button_loc = (By.XPATH, configdata.get_elementinfo(12))
    def add_save_button(self):
        """
        新增页面点击保存
        :return:
        """
        self.click(self.add_save_button_loc)

    click_export_button_loc = (By.XPATH, configdata.get_elementinfo(13))
    def click_export_button(self):
        """
        点击导出按钮
        :return:
        """
        self.click(self.click_export_button_loc)

    searchlist_number_loc = (By.XPATH, configdata.get_checkelementinfo(0))
    def searchlist_number(self):
        """
        返回查询结果列表的编号字段
        :return:
        """
        return self.find_presence_elem(self.searchlist_number_loc).text

    searchlist_addr_number_loc = (By.XPATH, configdata.get_checkelementinfo(1))
    def searchlist_addr_name(self):
        """
        返回查询结果列表的缩写字段
        :return:
        """
        return self.find_presence_elem(self.searchlist_addr_number_loc).text

    searchresult_count_loc = (By.XPATH, configdata.get_checkelementinfo(2))
    def searchresult_count(self):
        """
        返回查询结果列表的总条数
        :return:
        """
        return self.find_presence_elem(self.searchresult_count_loc).text

    add_success_loc = (By.CSS_SELECTOR, configdata.get_checkelementinfo(3))
    def add_success(self):
        """
        新增成功后返回保存成功字段
        :return:
        """
        return self.find_presence_elem(self.add_success_loc).text

    add_number_loc = (By.CSS_SELECTOR, configdata.get_checkelementinfo(4))
    def add_number(self):
        """
        新增页面获取市场大区编号字段
        :return:
        """
        return self.find_presence_elem(self.add_number_loc).text

    """组合操作"""
    def open_marketchannel(self):
        """
        进入市场大区页面
        :return:
        """
        self.click_ipc_select()
        self.click_channel()

    def search_marketchannel(self, number, abbr_name):
        """
        条件查询：按编号和缩写查询
        :return:
        """
        self.number(number)
        self.abbr_name(abbr_name)
        self.click_search_button()

    def add_marketchannel(self, add_abbr_name, add_cn_name, add_en_name, add_remark):
        """
        新增市场大区
        :return:
        """
        self.click_add_button()
        self.add_abbr_name(add_abbr_name)
        self.add_cn_name(add_cn_name)
        self.add_en_name(add_en_name)
        self.add_remark(add_remark)
        self.add_enable()
        sleep(1)
        mc_number = self.add_number()
        sleep(1)
        # DA = DataAssociation()
        # # print(mc_number)
        setattr(DA, 'mc_number', mc_number)
        print(getattr(DA, 'mc_number'))
        self.add_save_button()
        return mc_number


if __name__ == '__main__':
    from mdp_login import Login
    from public.models.getdriver import browser
    import logger
    from page.basepage import DataAssociation
    log = logger.Logs()
    username = 'david.luo'
    password = 'Ni&Li12345'
    driver = browser()
    case = Login(driver)
    case.login_user(username, password)
    case2 = MarketChannel(driver)

    case2.open_marketchannel()
    tt = case2.add_marketchannel("test141","测试11","test11","1111111111")
    # case2.search_marketchannel('MC0001', 'CN')
    # print(case2.searchlist_number())
    log.info(tt)
    print(tt)
    a = DataAssociation()
    setattr(a, 'mc', tt)
    print(hasattr(a, 'mc'))
    # add = case2.add_success()
    # print(add)
    getattr(DataAssociation(), 'mc')
    print(getattr(DataAssociation(), 'mc'))
    # log.info(case2.searchlist_addr_name())