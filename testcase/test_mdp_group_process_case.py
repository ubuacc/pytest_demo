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
        MarketGroup(self.driver).add_marketgroup(mc, abbr_name, cn_name, en_name, mark)

    def modify_marketgroup(self, modify_mc, modify_cn_name, modify_en_name, modify_mark):
        MarketGroup(self.driver).modify_marketgroup(modify_mc, modify_cn_name, modify_en_name, modify_mark)

    def test_marketgroup(self):
        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[0]['id'], testdata_process[0]['detail']))
        # 调用新增市场大区函数
        po = MarketGroup(self.driver)
        mc_add_abbr_name = getattr(DA, 'mc_add_abbr_name')
        mg_add_abbr_name = testdata_process[0]['data']['add_abbr_name'] + str(int(time.time()))
        setattr(DA, 'mg_add_abbr_name', mg_add_abbr_name)
        self.add_marketgroup(mc_add_abbr_name, mg_add_abbr_name, testdata_process[0]['data']['add_cn_name'], testdata_process[0]['data']['add_en_name'], testdata_process[0]['data']['add_mark'])
        sleep(1.5)
        mg_number = getattr(DA, 'mg_number')
        self.assertEqual(testdata_process[0]['check'][0], po.add_success())
        self.log.info("新增成功，返回实际结果是->: {}".format(po.add_success()))
        screenshot.screenshot(self.driver, testdata_process[0]['screenshot'])

        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[1]['id'], testdata_process[1]['detail']))
        # 调用查询方法
        self.search_marketgroup(mc_add_abbr_name, mg_number, mg_add_abbr_name)
        sleep(3)
        self.assertEqual(mc_add_abbr_name, po.checklist_mc())
        self.log.info("查询成功，返回依赖的市场大区缩写字段实际结果是->: {}".format(po.checklist_mc()))
        self.assertEqual(mg_number, po.checklist_number())
        self.log.info("查询成功，返回市场群编号字段实际结果是->: {}".format(po.checklist_number()))
        self.assertEqual(mg_add_abbr_name, po.checklist_abbr_name())
        self.log.info("查询成功，返回市场群缩写字段实际结果是->: {}".format(po.checklist_abbr_name()))
        self.assertEqual(testdata_process[1]['check'][3], po.searchlist_cn_name())
        self.log.info("查询成功，返回市场群中文名字段实际结果是->: {}".format(po.searchlist_cn_name()))
        self.assertEqual(testdata_process[1]['check'][4], po.searchlist_en_name())
        self.log.info("查询成功，返回市场群中文名字段实际结果是->: {}".format(po.searchlist_en_name()))
        screenshot.screenshot(self.driver, testdata_process[1]['screenshot'])

        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[2]['id'], testdata_process[2]['detail']))
        # 调用修改市场大区函数
        self.modify_marketgroup(mc_add_abbr_name, testdata_process[2]['data']['modify_cn_name'], testdata_process[2]['data']['modify_en_name'], testdata_process[2]['data']['modify_mark'])
        sleep(1.5)
        self.assertEqual(testdata_process[2]['check'][0], po.modify_success())
        self.log.info("修改成功，返回实际结果是->: {}".format(po.modify_success()))
        screenshot.screenshot(self.driver, testdata_process[2]['screenshot'])

        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[3]['id'], testdata_process[3]['detail']))
        # 调用查询市场大区函数
        self.search_marketgroup(mc_add_abbr_name, mg_number, mg_add_abbr_name)
        sleep(3)
        self.assertEqual(testdata_process[3]['check'][0], po.searchlist_cn_name())
        self.log.info("查询成功，返回市场大区中文名字段实际结果是->: {}".format(po.searchlist_cn_name()))
        self.assertEqual(testdata_process[3]['check'][1], po.searchlist_en_name())
        self.log.info("查询成功，返回市场大区中文名字段实际结果是->: {}".format(po.searchlist_en_name()))
        screenshot.screenshot(self.driver, testdata_process[1]['screenshot'])

