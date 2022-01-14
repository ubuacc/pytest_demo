#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/1/6 14:19
import unittest

from public.page.test_mdp_login import Login
from public.models.getyaml import YamlRead
from public.models import myunit,logger,screenshot
import unittest
import os
from config import setting

testdata = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'testdata_login.yaml')).yaml_all()


class TestLogin(myunit.TestUnit):
    '''登录测试'''

    def user_login(self, username, password):
        Login(self.driver).test_login_user(username, password)


    def loginout(self):
        Login(self.driver).loginout()

    def test_login(self,testdata):
        """
        登录测试
        :param testdata: 加载testdata_login登录测试数据
        :return:
        """
        log = logger.Logs()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(testdata['id'],testdata['detail']))
        # 调用登录方法
        self.user_login(testdata['data']['phone'],testdata['data']['password'])
        po = Login(self.driver)
        if testdata['screenshot'] == 'phone_pawd_success':
            log.info("检查点-> {0}".format(Login(self.driver).login_success()))
            self.assertEqual(po.login_success(), testdata['check'][0], "成功登录，返回实际结果是->: {0}".format(po.login_success()))
            log.info("成功登录，返回实际结果是->: {0}".format(po.login_success()))
            screenshot.screenshot(self.driver, testdata['screenshot'])
            log.info("-----> 开始执行退出流程操作")
            self.loginout()
            po_exit = Login(self.driver)
            log.info("检查点-> 找到{0}元素,表示退出成功！".format(po_exit.loginout()))
            self.assertEqual(po_exit.loginout(), "退出登录，返回实际结果是->: {0}".format(po_exit.loginout()))
            log.info("退出登录，返回实际结果是->: {0}".format(po_exit.loginout()))
        else:
            log.info("检查点-> {0}".format(po.login_failure()))
            self.assertEqual(po.login_failure(),testdata['check'][0] , "异常登录，返回实际结果是->: {0}".format(po.login_failure()))
            log.info("异常登录，返回实际结果是->: {0}".format(po.login_failure()))
            screenshot.screenshot(self.driver, testdata['screenshot'])

