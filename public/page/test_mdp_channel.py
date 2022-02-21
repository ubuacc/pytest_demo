#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/2/17 15:44
import os
from public.models.getdriver import browser
from selenium.webdriver.common.by import By
from public.page.basepage import BasePage
from public.models.getyaml import YamlRead
from config import setting

configdata = YamlRead(os.path.join(setting.TEST_Element_YAML, 'ipc_marketchannel.yaml'))


class TestMarketChannel(BasePage):

    ipc_select_loc = (By.XPATH, configdata.get_elementinfo(0))
    def test_click_ipc_select(self):
        """
        点击IPC主数据下拉框
        :return:
        """
        self.find_clickable_elem(self.ipc_select_loc).click()

    channel_loc = (By.XPATH, configdata.get_elementinfo(1))
    def test_click_channel(self):
        """
        点击市场大区进入市场大区页面
        :return:
        """
        self.find_clickable_elem(self.channel_loc).click()

    number_loc = (By.XPATH, configdata.get_elementinfo(2))
    def number(self, number):
        """
        输入编号
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

    add_save_button_loc = (By.XPATH, configdata.get_elementinfo(10))
    def add_save_button(self):
        """
        新增页面点击保存
        :return:
        """
        self.click(self.add_save_button())
        
    click_export_button_loc = (By.XPATH, configdata.get_elementinfo(6))
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

    """组合操作"""
    def search(self):
        pass

if __name__ == '__main__':
    from test_mdp_login import TestLogin
    from public.models.getdriver import browser
    username = 'david.luo'
    password = 'Ni&Li12345'
    driver = browser()
    case = TestLogin(driver)
    case.test_login_user(username, password)
    case2 = TestMarketChannel(driver)
    case2.test_click_ipc_select()
    case2.test_click_channel()
    case2.abbr_name('cn')
    case2.click_search_button()