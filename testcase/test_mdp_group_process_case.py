#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/3/28 11:02
import time
from time import sleep

from public.page.mdp_ipc_group import MarketGroup
from public.page.mdp_ipc_channel import DA
from public.page.mdp_login import Login
from public.models.getyaml import YamlRead
from public.models import myunit, logger, screenshot
import os
from config import setting

f = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'login.yaml')).yaml_all()
username = f[4]['data']['username']
password = f[4]['data']['password']

testdata_process = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'marketgroup_process.yaml')).yaml_all()


class TestMarketGroup(myunit.TestUnit):

    @classmethod
    def setUpClass(cls):
        super(TestMarketGroup, cls).setUpClass()
        Login(cls.driver).login_user(username, password)
        cls.log = logger.Logs()
        MarketGroup(cls.driver).open_marketgroup()

    def search_marketgroup(self, mc, number_mg, abbr_name_mg):
        MarketGroup(self.driver).search_marketgroup(mc, number_mg, abbr_name_mg)

    def add_marketgroup(self, mc, abbr_name, cn_name, en_name, mark):
        return MarketGroup(self.driver).add_marketgroup(mc, abbr_name, cn_name, en_name, mark)

    def test_marketgroup(self):
        self.log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(testdata_process[0]['id'], testdata_process[0]['detail']))
        # 调用新增市场大区函数
        po = MarketGroup(self.driver)
        add_abbr_name = testdata_process[0]['data']['add_abbr_name'] + str(int(time.time()))
        mc = getattr(DA, 'mc_add_abbr_name')
        self.log.info(mc)
        number = self.add_marketgroup(mc, add_abbr_name, testdata_process[0]['data']['add_cn_name'], testdata_process[0]['data']['add_en_name'], testdata_process[0]['data']['add_mark'])
        sleep(1.5)
        self.assertEqual(testdata_process[0]['check'][0], po.add_success(), "新增成功，返回实际结果是->: {}".format(po.add_success()))
        self.log.info("新增成功，返回实际结果是->: {}".format(po.add_success()))
        screenshot.screenshot(self.driver, testdata_process[0]['screenshot'])

        self.log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(testdata_process[1]['id'], testdata_process[1]['detail']))
        # 调用查询方法
        self.search_marketgroup(mc, number, add_abbr_name)
        sleep(3)
        self.assertEqual(mc, po.checklist_mc(), "查询成功，返回实际结果是->: {}".format(po.checklist_mc()))
        self.log.info("查询成功，返回实际结果是->: {}".format(po.checklist_mc()))
        self.assertEqual(number, po.checklist_number(), "查询成功，返回实际结果是->: {}".format(po.checklist_number()))
        self.log.info("查询成功，返回实际结果是->: {}".format(po.checklist_number()))
        self.assertEqual(add_abbr_name, po.checklist_abbr_name(), "查询成功，返回实际结果是->: {}".format(po.checklist_abbr_name()))
        self.log.info("查询成功，返回实际结果是->: {}".format(po.checklist_abbr_name()))
        screenshot.screenshot(self.driver, testdata_process[1]['screenshot'])

