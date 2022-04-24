#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/4/2 9:33
import time
import unittest
from time import sleep

from public.page.mdp_ipc_channel import MarketChannel
from public.page.mdp_login import Login
from public.models.getyaml import YamlRead
from public.page.basepage import DA
from public.models import myunit, logger, screenshot
import os
from config import setting

f = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'login.yaml')).yaml_all()
username = f[4]['data']['username']
password = f[4]['data']['password']

testdata_process = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'marketchannel_process.yaml')).yaml_all()

class TestMarketChannelProcess(myunit.TestUnit):

    @classmethod
    def setUpClass(cls):
        super(TestMarketChannelProcess, cls).setUpClass()
        Login(cls.driver).login_user(username, password)
        cls.log = logger.Logs()
        MarketChannel(cls.driver).open_marketchannel()

    def search_marketchannel(self, number, abbr_name):
        MarketChannel(self.driver).search_marketchannel(number, abbr_name)

    def add_marketchannel(self, add_abbr_name, add_cn_name, add_en_name, add_mark):
        MarketChannel(self.driver).add_marketchannel(add_abbr_name, add_cn_name, add_en_name, add_mark)

    def modify_marketchannel(self, modify_cn_name, modify_en_name, modify_mark):
        MarketChannel(self.driver).modify_marketchannel(modify_cn_name, modify_en_name, modify_mark)

    def test_marketchannel_process(self):
        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[0]['id'], testdata_process[0]['detail']))
        # 调用新增市场大区函数
        po = MarketChannel(self.driver)
        add_abbr_name = testdata_process[0]['data']['add_abbr_name'] + str(int(time.time()))
        setattr(DA, 'mc_add_abbr_name', add_abbr_name)
        self.add_marketchannel(add_abbr_name, testdata_process[0]['data']['add_cn_name'], testdata_process[0]['data']['add_en_name'], testdata_process[0]['data']['add_mark'])
        mc_number = getattr(DA, 'mc_number')
        sleep(1.5)
        self.assertEqual(testdata_process[0]['check'][0], po.add_success())
        self.log.info("新增成功，返回实际结果是->: {}".format(po.add_success()))
        screenshot.screenshot(self.driver, testdata_process[0]['screenshot'])

        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[1]['id'], testdata_process[1]['detail']))
        # 调用查询市场大区方法
        self.search_marketchannel(mc_number, add_abbr_name)
        sleep(3)
        self.assertEqual(mc_number, po.searchlist_number())
        self.log.info("查询成功，返回市场大区编号字段实际结果是->: {}".format(po.searchlist_number()))
        self.assertEqual(add_abbr_name, po.searchlist_addr_name())
        self.log.info("查询成功，返回市场大区缩写字段实际结果是->: {}".format(po.searchlist_addr_name()))
        self.assertEqual(testdata_process[1]['check'][2], po.searchlist_cn_name())
        self.log.info("查询成功，返回市场大区中文名字段实际结果是->: {}".format(po.searchlist_cn_name()))
        self.assertEqual(testdata_process[1]['check'][3], po.searchlist_en_name())
        self.log.info("查询成功，返回市场大区中文名字段实际结果是->: {}".format(po.searchlist_en_name()))
        screenshot.screenshot(self.driver, testdata_process[1]['screenshot'])

        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[2]['id'], testdata_process[2]['detail']))
        # 调用修改市场大区函数
        self.modify_marketchannel(testdata_process[2]['data']['modify_cn_name'], testdata_process[2]['data']['modify_en_name'], testdata_process[2]['data']['modify_mark'])
        sleep(1.5)
        self.assertEqual(testdata_process[2]['check'][0], po.modify_success())
        self.log.info("修改成功，返回实际结果是->: {}".format(po.modify_success()))
        screenshot.screenshot(self.driver, testdata_process[2]['screenshot'])

        self.log.info("当前执行测试流程ID-> {0} ; 测试流程-> {1}".format(testdata_process[3]['id'], testdata_process[3]['detail']))
        # 调用查询市场大区函数
        self.search_marketchannel(mc_number, add_abbr_name)
        sleep(3)
        self.assertEqual(testdata_process[3]['check'][0], po.searchlist_cn_name())
        self.log.info("查询成功，返回市场大区中文名字段实际结果是->: {}".format(po.searchlist_cn_name()))
        self.assertEqual(testdata_process[3]['check'][1], po.searchlist_en_name())
        self.log.info("查询成功，返回市场大区中文名字段实际结果是->: {}".format(po.searchlist_en_name()))
        screenshot.screenshot(self.driver, testdata_process[1]['screenshot'])

if __name__ == '__main__':
    unittest.main()
