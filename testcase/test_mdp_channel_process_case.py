#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/4/2 9:33
import time
from time import sleep

from public.page.mdp_ipc_channel import MarketChannel
from public.page.mdp_login import Login
from public.models.getyaml import YamlRead
from page.mdp_ipc_channel import DA
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
        return MarketChannel(self.driver).add_marketchannel(add_abbr_name, add_cn_name, add_en_name, add_mark)

    def test_marketchannel_process(self):
        self.log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(testdata_process[0]['id'], testdata_process[0]['detail']))
        # 调用新增市场函数
        po = MarketChannel(self.driver)
        add_abbr_name = testdata_process[0]['data']['add_abbr_name'] + str(int(time.time()))
        print(add_abbr_name)
        setattr(DA, 'mc_add_abbr_name', add_abbr_name)
        print(getattr(DA, 'mc_add_abbr_name'))
        number = self.add_marketchannel(add_abbr_name,
                                        testdata_process[0]['data']['add_cn_name'],
                                        testdata_process[0]['data']['add_en_name'],
                                        testdata_process[0]['data']['add_mark'])
        sleep(1.5)
        self.assertEqual(testdata_process[0]['check'][0], po.add_success(), "新增成功，返回实际结果是->: {}".format(po.add_success()))
        self.log.info("新增成功，返回实际结果是->: {}".format(po.add_success()))
        print(getattr(DA, 'mc_number'))
        screenshot.screenshot(self.driver, testdata_process[0]['screenshot'])

        self.log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(testdata_process[1]['id'], testdata_process[1]['detail']))
        # 调用查询方法
        self.search_marketchannel(number, add_abbr_name)
        sleep(3)
        self.assertEqual(number, po.searchlist_number(), "查询成功，返回实际结果是->: {}".format(po.searchlist_number()))
        self.log.info("查询成功，返回实际结果是->: {}".format(po.searchlist_number()))
        self.assertEqual(add_abbr_name, po.searchlist_addr_name(), "查询成功，返回实际结果是->: {}".format(po.searchlist_addr_name()))
        self.log.info("查询成功，返回实际结果是->: {}".format(po.searchlist_addr_name()))


