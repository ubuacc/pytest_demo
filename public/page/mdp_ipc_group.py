#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/3/21 14:10

import os
from selenium.webdriver.common.by import By


from public.page.basepage import BasePage
from public.models.getyaml import YamlRead
from config import setting

configdata = YamlRead(os.path.join(setting.TEST_Element_YAML, 'ipc_marketgroup.yaml'))

class MarketGroup(BasePage):

    ipc_select_loc = (By.XPATH, configdata.get_elementinfo(0))
    def click_ipc_select(self):
        """
        点击IPC主数据下拉框
        :return:
        """
        self.find_clickable_elem(self.ipc_select_loc).click()

    market_group_loc = (By.XPATH, configdata.get_elementinfo(1))
    def click_market_group(self):
        """
        点击市场群进入市场群页面
        :return:
        """
        self.find_clickable_elem(self.market_group_loc).click()

    click_mc_select_loc = (By.XPATH, configdata.get_elementinfo(2))
    def click_mc_select(self, mc):
        """
        点击市场大区下拉框
        :return:
        """
        self.send_keys(self.click_mc_select_loc, mc)

    click_marketchannel_loc = (By.CSS_SELECTOR, configdata.get_elementinfo(3))
    def click_marketchannel(self):
        """
        点击选择市场大区
        :return:
        """
        self.click(self.click_marketchannel_loc)

    number_mg_loc = (By.XPATH, configdata.get_elementinfo(4))
    def number_mg(self, number_mg):
        """
        输入市场群编号
        :return:
        """
        self.send_keys(self.number_mg_loc, number_mg)

    abbr_name_mg_loc = (By.XPATH, configdata.get_elementinfo(5))
    def abbr_name_mg(self, abbr_name_mg):
        """
        输入市场群缩写
        :return:
        """
        self.send_keys(self.abbr_name_mg_loc, abbr_name_mg)

    click_search_button_mg_loc = (By.XPATH, configdata.get_elementinfo(6))
    def click_search_button_mg(self):
        """
        点击查询按钮
        :return:
        """
        self.click(self.click_search_button_mg_loc)

    click_add_button_mg_loc = (By.XPATH, configdata.get_elementinfo(7))
    def click_add_button_mg(self):
        """
        点击添加按钮
        :return:
        """
        self.click(self.click_add_button_mg_loc)

    add_number_loc = (By.CSS_SELECTOR, configdata.get_checkelementinfo(0))
    def add_number(self):
        """
        返回新增页面的编号字段
        :return:
        """
        return self.find_presence_elem(self.add_number_loc).text

    add_click_mc_select_loc = (By.XPATH, configdata.get_elementinfo(8))
    def add_click_mc_select(self):
        """
        新增页面点击市场大区下拉框
        :return:
        """
        self.find_clickable_elem(self.add_click_mc_select_loc).click()

    add_sendkeys_mc_select_loc = (By.XPATH, configdata.get_elementinfo(9))
    def add_sendkeys_mc_select(self, mc):
        """
        新增页面市场大区下拉框输入市场大区模糊搜索
        :return:
        """
        self.send_keys(self.add_sendkeys_mc_select_loc, mc)

    add_click_marketchannel_loc = (By.CSS_SELECTOR, configdata.get_elementinfo(10))
    def add_click_marketchannel(self):
        """
        新增页面点击选择模糊搜索后的市场大区
        :return:
        """
        self.click(self.add_click_marketchannel_loc)

    add_abbr_name_loc = (By.XPATH, configdata.get_elementinfo(11))
    def add_abbr_name(self, abbr_name):
        """
        新增页面输入缩写
        :return:
        """
        self.send_keys(self.add_abbr_name_loc, abbr_name)

    add_cn_name_loc = (By.XPATH, configdata.get_elementinfo(12))
    def add_cn_name(self, cn_name):
        """
        新增页面输入中文名
        :return:
        """
        self.send_keys(self.add_cn_name_loc, cn_name)

    add_en_name_loc = (By.XPATH, configdata.get_elementinfo(13))
    def add_en_name(self, en_name):
        """
        新增页面输入英文名
        :param en_name:
        :return:
        """
        self.send_keys(self.add_en_name_loc,en_name)

    add_mark_loc = (By.XPATH, configdata.get_elementinfo(14))
    def add_mark(self, mark):
        """
        新增页面输入描述
        :return:
        """
        self.send_keys(self.add_mark_loc, mark)

    add_enable_loc = (By.XPATH, configdata.get_elementinfo(15))
    def add_enable(self):
        """
        新增页面启用状态
        :return:
        """
        self.click(self.add_enable_loc)

    add_disable_loc = (By.XPATH, configdata.get_elementinfo(16))
    def add_disable(self):
        """
        新增页面禁用状态
        :return:
        """
        self.click(self.add_disable_loc)

    add_save_button_loc = (By.XPATH, configdata.get_elementinfo(17))
    def add_save_button(self):
        """
        新增页面点击保存
        :return:
        """
        self.find_clickable_elem(self.add_save_button_loc).click()

    click_export_button_loc = (By.XPATH, configdata.get_elementinfo(18))
    def click_export_button(self):
        """
        点击导出按钮
        :return:
        """
        self.click(self.click_export_button_loc)

    checklist_mc_loc = (By.XPATH, configdata.get_checkelementinfo(1))
    def checklist_mc(self):
        """
        返回查询列表的第一条数据的市场大区字段
        :return:
        """
        return self.find_presence_elem(self.checklist_mc_loc).text

    checklist_number_loc = (By.XPATH, configdata.get_checkelementinfo(2))
    def checklist_number(self):
        """
        返回查询列表的第一条数据的编号字段
        :return:
        """
        return self.find_presence_elem(self.checklist_number_loc).text

    checklist_abbr_name_loc = (By.XPATH, configdata.get_checkelementinfo(3))
    def checklist_abbr_name(self):
        """
        返回查询列表的第一条数据的缩写字段
        :return:
        """
        return self.find_presence_elem(self.checklist_abbr_name_loc).text

    searchresult_count_loc = (By.XPATH, configdata.get_checkelementinfo(4))
    def searchresult_count(self):
        """
        返回查询列表总条数
        :return:
        """
        return self.find_presence_elem(self.searchresult_count_loc).text

    add_success_loc = (By.XPATH, configdata.get_checkelementinfo(5))
    def add_success(self):
        """
        返回新增页面保存成功字段
        :return:
        """
        return self.find_presence_elem(self.add_success_loc).text

    """组合操作"""
    def open_marketgroup(self):
        """
        打开市场群页面
        :return:
        """
        self.click_ipc_select()
        self.click_market_group()

    def search_marketgroup(self, mc, number_mg, abbr_name_mg):
        """
        市场群查询
        :return:
        """
        self.click_mc_select(mc)
        self.click_marketchannel()
        self.number_mg(number_mg)
        self.abbr_name_mg(abbr_name_mg)
        self.click_search_button_mg()

    def add_marketgroup(self, mc, abbr_name, cn_name, en_name, mark):
        """
        新增市场群
        :return:
        """
        self.click_add_button_mg()
        self.add_click_mc_select()
        self.add_sendkeys_mc_select(mc)
        self.add_click_marketchannel()
        self.add_abbr_name(abbr_name)
        self.add_cn_name(cn_name)
        self.add_en_name(en_name)
        self.add_mark(mark)
        self.add_enable()
        num = self.add_number()
        self.add_save_button()
        return num



if __name__ == '__main__':
    from mdp_login import Login
    from public.models.getdriver import browser
    import logger
    from time import sleep
    from selenium.webdriver.support.select import Select
    log = logger.Logs()
    username = 'david.luo'
    password = 'Ni&Li12345'
    driver = browser()
    case = Login(driver)
    case.login_user(username, password)
    case2 = MarketGroup(driver)
    case2.open_marketgroup()
    # case2.search_marketgroup('cn', '','test001')
    num = case2.add_marketgroup('cn', 'test007', 'test007', 'test007', 'test07')
    print(num)
    print(type(num))
    # case2.click_add_button_mg()
    # sleep(1)
    # case2.click_sele()
    # case2.add_click_mc_select('cn')
    # case2.click_mc_select('cn')
    # case2.add_cn_name('test0001')
    # case2.add_click_mc_select('cn')
