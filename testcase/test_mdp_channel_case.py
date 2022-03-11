#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/2/22 9:45
from time import sleep

from getdriver import browser
from public.page.test_mdp_channel import MarketChannel
from public.page.test_mdp_login import Login
from public.models.getyaml import YamlRead
from public.models import myunit, logger, screenshot
import os, ddt
from config import setting

f = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'testdata_login.yaml')).yaml_all()
username = f[4]['data']['username']
password = f[4]['data']['password']

testdata = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'testdata_marketchannel.yaml')).yaml_all()

@ddt.ddt
class TestMarketChannel(myunit.TestUnit):

    @classmethod
    def setUpClass(cls):
        super(TestMarketChannel, cls).setUpClass()
        Login(cls.driver).login_user(username, password)
        MarketChannel(cls.driver).open_marketchannel()

    # def open_marketchannel(self):
    #     MarketChannel(self.driver).open_marketchannel()

    def search_marketchannel(self, number, abbr_name):
        MarketChannel(self.driver).search_marketchannel(number, abbr_name)

    def add_marketchanner(self, add_abbr_name, add_cn_name, add_en_name, add_mark):
        MarketChannel(self.driver).add_marketchannel(add_abbr_name, add_cn_name, add_en_name, add_mark)

    @ddt.data(*testdata)
    def test_search_marketchannel(self, testdata):
        '''
        市场大区查询测试
        :return:
        '''
        log = logger.Logs()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(testdata['id'], testdata['detail']))
        # 调用查询方法
        sleep(3)
        self.search_marketchannel(testdata['data']['number'], testdata['data']['abbr_name'])
        sleep(3)
        po = MarketChannel(self.driver)
        if testdata['screenshot'] == 'number_abbrname_empty':
            log.info("检查点-> {0}".format(po.searchresult_count()))
            self.assertNotIn(testdata['check'][0], po.searchresult_count(), "查询成功，返回实际结果是->: {}".format(po.searchresult_count()))
            log.info("查询成功，返回实际结果是->: {0}".format(po.searchresult_count()))
            screenshot.screenshot(self.driver, testdata['screenshot'])
        elif testdata['screenshot'] == 'abbrname_empty':
            log.info("检查点-> {0}".format(po.searchlist_number()))
            self.assertEqual(testdata['check'][0], po.searchlist_number(), "查询成功，返回实际结果是->: {}".format(po.searchlist_number()))
            log.info("查询成功，返回实际结果是->: {0}".format(po.searchlist_number()))
            screenshot.screenshot(self.driver, testdata['screenshot'])
        elif testdata['screenshot'] == 'number_empty':
            log.info("检查点-> {0}".format(po.searchlist_addr_name()))
            self.assertEqual(testdata['check'][0], po.searchlist_addr_name(), "查询成功，返回实际结果是->: {}".format(po.searchlist_addr_name()))
            log.info("查询成功，返回实际结果是->: {}".format(po.searchlist_addr_name()))
            screenshot.screenshot(self.driver, testdata['screenshot'])