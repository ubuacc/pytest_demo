#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/1/6 14:19

from public.page.mdp_login import Login
from public.models.getyaml import YamlRead
from public.models import myunit,logger,screenshot
import os, ddt
from config import setting



testdata = YamlRead(os.path.join(setting.TEST_DATA_YAML, 'login.yaml')).yaml_all()


@ddt.ddt
class TestLogin(myunit.TestUnit):
    '''登录测试'''

    def user_login(self,username,password):
        Login(self.driver).login_user(username, password)


    def loginout(self):
        Login(self.driver).login_exit()

    @ddt.data(*testdata)
    def test_login(self,testdata):
        """
        登录测试
        :param testdata: 加载testdata_login登录测试数据
        :return:
        """
        log = logger.Logs()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(testdata['id'],testdata['detail']))
        # 调用登录方法
        self.user_login(testdata['data']['username'],testdata['data']['password'])
        po = Login(self.driver)
        if testdata['screenshot'] == 'username_pawd_success':
            log.info("检查点-> {0}".format(Login(self.driver).login_success()))
            self.assertEqual(po.login_success(), testdata['check'][0], "成功登录，返回实际结果是->: {0}".format(po.login_success()))
            log.info("成功登录，返回实际结果是->: {0}".format(po.login_success()))
            screenshot.screenshot(self.driver, testdata['screenshot'])
            log.info("-----> 开始执行退出流程操作")
            self.loginout()
            po_exit = Login(self.driver)
            log.info("检查点-> 找到{0}元素,表示退出成功！".format(po_exit.loginout()))
            self.assertEqual(po_exit.loginout(),testdata['check'][1] ,"退出登录，返回实际结果是->: {0}".format(po_exit.loginout()))
            log.info("退出登录，返回实际结果是->: {0}".format(po_exit.loginout()))
        elif testdata['screenshot'] == 'username_pawd_empty':
            log.info("检查点-> {0},{1}".format(po.login_username_empty(),po.login_password_empty()))
            self.assertEqual(po.login_username_empty(), testdata['check'][0], "登录失败，返回实际结果是->: {}".format(po.login_username_empty()))
            self.assertEqual(po.login_password_empty(), testdata['check'][1], "登录失败，返回实际结果是->: {}".format(po.login_password_empty()))
            log.info("登录失败，返回实际结果是->: {},{}".format(po.login_username_empty(),po.login_password_empty()))
            screenshot.screenshot(self.driver,testdata['screenshot'])
        elif testdata['screenshot'] == 'username_empty':
            log.info("检查点-> {0}".format(po.login_username_empty()))
            self.assertEqual(po.login_username_empty(), testdata['check'][0], "登录失败，返回实际结果是->: {}".format(po.login_username_empty()))
            log.info("登录失败，返回实际结果是->: {}".format(po.login_username_empty()))
            screenshot.screenshot(self.driver,testdata['screenshot'])
        elif testdata['screenshot'] == 'password_empty':
            log.info("检查点-> {0}".format(po.login_password_empty()))
            self.assertEqual(po.login_password_empty(),testdata['check'][0],"登录失败，返回实际结果是->: {}".format(po.login_password_empty()))
            log.info("登录失败，返回实际结果是->: {}".format(po.login_password_empty()))
            screenshot.screenshot(self.driver,testdata['screenshot'])
        else:
            log.info("检查点-> {0}".format(po.login_failure()))
            self.assertIn(testdata['check'][0],po.login_failure(), "异常登录，返回实际结果是->: {0}".format(po.login_failure()))
            log.info("异常登录，返回实际结果是->: {0}".format(po.login_failure()))
            screenshot.screenshot(self.driver, testdata['screenshot'])



