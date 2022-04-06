#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/4/1 10:17
import time
from time import sleep

from public.page.mdp_ipc_place import MarketPlace
from public.page.mdp_login import Login
from public.models.getyaml import YamlRead
from public.models import myunit, logger, screenshot
import os, ddt
from config import setting

f = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'login.yaml')).yaml_all()
username = f[4]['data']['username']
password = f[4]['data']['password']

testdata_process = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'marketplace_process.yaml')).yaml_all()


class TestMarketPlace(myunit.TestUnit):

    @classmethod
    def setUpClass(cls):
        super(TestMarketPlace, cls).setUpClass()
        Login(cls.driver).login_user(username, password)
        cls.log = logger.Logs()
        MarketPlace(cls.driver).open_marketplace()

    def search_marketplace(self, mp, number_mg, abbr_name_mg):
        MarketPlace(self.driver).search_marketplace(mp, number_mg, abbr_name_mg)

    def add_marketplace(self, mg, abbr_name, cn_name, en_name, mark):
        return MarketPlace(self.driver).add_marketplace(mg, abbr_name, cn_name, en_name, mark)

    def test_marketplace(self):
        self.log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(testdata_process[0]['id'], testdata_process[0]['detail']))
        # 调用新增市场函数
        po = MarketPlace(self.driver)
        add_abbr_name = testdata_process[0]['data']['add_abbr_name'] + str(int(time.time()))
        number = self.add_marketplace(testdata_process[0]['data']['mg'], add_abbr_name, testdata_process[0]['data']['add_cn_name'], testdata_process[0]['data']['add_en_name'], testdata_process[0]['data']['add_mark'])
        sleep(1.5)
        self.assertEqual(testdata_process[0]['check'][0], po.add_success(), "新增成功，返回实际结果是->: {}".format(po.add_success()))
        self.log.info("新增成功，返回实际结果是->: {}".format(po.add_success()))
        screenshot.screenshot(self.driver, testdata_process[0]['screenshot'])

        self.log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(testdata_process[1]['id'], testdata_process[1]['detail']))
        # 调用查询方法
        self.search_marketplace(testdata_process[1]['data']['mg'], number, add_abbr_name)
        sleep(3)
        self.assertEqual(testdata_process[1]['data']['mg'], po.checklist_mg(), "查询成功，返回实际结果是->: {}".format(po.checklist_mg()))
        self.log.info("查询成功，返回实际结果是->: {}".format(po.checklist_mg()))
        self.assertEqual(number, po.checklist_number(), "查询成功，返回实际结果是->: {}".format(po.checklist_number()))
        self.log.info("查询成功，返回实际结果是->: {}".format(po.checklist_number()))
        self.assertEqual(add_abbr_name, po.checklist_abbr_name(), "查询成功，返回实际结果是->: {}".format(po.checklist_abbr_name()))
        self.log.info("查询成功，返回实际结果是->: {}".format(po.checklist_abbr_name()))