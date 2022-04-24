#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/4/1 10:17
import time
from time import sleep

from public.page.basepage import DA
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
        MarketPlace(self.driver).add_marketplace(mg, abbr_name, cn_name, en_name, mark)

    def modify_marketplace(self, modify_mg, modify_cn_name, modify_en_name, modify_mark):
        MarketPlace(self.driver).modify_marketplace(modify_mg, modify_cn_name, modify_en_name, modify_mark)

    def test_marketplace(self):
        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[0]['id'], testdata_process[0]['detail']))
        # 调用新增市场函数
        po = MarketPlace(self.driver)
        mp_add_abbr_name = testdata_process[0]['data']['add_abbr_name'] + str(int(time.time()))
        mg_add_abbr_name = getattr(DA, 'mg_add_abbr_name')
        self.add_marketplace(mg_add_abbr_name, mp_add_abbr_name, testdata_process[0]['data']['add_cn_name'], testdata_process[0]['data']['add_en_name'], testdata_process[0]['data']['add_mark'])
        sleep(1.5)
        mp_number = getattr(DA, 'mp_number')
        self.assertEqual(testdata_process[0]['check'][0], po.add_success())
        self.log.info("新增成功，返回实际结果是->: {}".format(po.add_success()))
        screenshot.screenshot(self.driver, testdata_process[0]['screenshot'])

        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[1]['id'], testdata_process[1]['detail']))
        # 调用查询方法
        self.search_marketplace(mg_add_abbr_name, mp_number, mp_add_abbr_name)
        sleep(3)
        self.assertEqual(mg_add_abbr_name, po.checklist_mg())
        self.log.info("查询成功，返回市场群缩写字段实际结果是->: {}".format(po.checklist_mg()))
        self.assertEqual(mp_number, po.checklist_number())
        self.log.info("查询成功，返回市场编号字段实际结果是->: {}".format(po.checklist_number()))
        self.assertEqual(mp_add_abbr_name, po.checklist_abbr_name())
        self.log.info("查询成功，返回市场缩写字段实际结果是->: {}".format(po.checklist_abbr_name()))
        self.assertEqual(testdata_process[1]['check'][3], po.searchlist_cn_name())
        self.log.info("查询成功，返回市场群中文名字段实际结果是->: {}".format(po.searchlist_cn_name()))
        self.assertEqual(testdata_process[1]['check'][4], po.searchlist_en_name())
        self.log.info("查询成功，返回市场群中文名字段实际结果是->: {}".format(po.searchlist_en_name()))
        screenshot.screenshot(self.driver, testdata_process[1]['screenshot'])

        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[2]['id'], testdata_process[2]['detail']))
        # 调用修改市场大区函数
        self.modify_marketplace(mg_add_abbr_name, testdata_process[2]['data']['modify_cn_name'],
                                testdata_process[2]['data']['modify_en_name'],
                                testdata_process[2]['data']['modify_mark'])
        sleep(1.5)
        self.assertEqual(testdata_process[2]['check'][0], po.modify_success())
        self.log.info("修改成功，返回实际结果是->: {}".format(po.modify_success()))
        screenshot.screenshot(self.driver, testdata_process[2]['screenshot'])

        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[3]['id'], testdata_process[3]['detail']))
        # 调用查询市场大区函数
        self.search_marketplace(mg_add_abbr_name, mp_number, mp_add_abbr_name)
        sleep(3)
        self.assertEqual(testdata_process[3]['check'][0], po.searchlist_cn_name())
        self.log.info("查询成功，返回市场大区中文名字段实际结果是->: {}".format(po.searchlist_cn_name()))
        self.assertEqual(testdata_process[3]['check'][1], po.searchlist_en_name())
        self.log.info("查询成功，返回市场大区中文名字段实际结果是->: {}".format(po.searchlist_en_name()))
        screenshot.screenshot(self.driver, testdata_process[1]['screenshot'])