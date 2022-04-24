#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time:  10:08
import configparser
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public.models.logger import Logs
from config import setting
from selenium.webdriver.common.action_chains import ActionChains

con = configparser.ConfigParser()
con.read(setting.CONFIG_DIR,encoding='utf-8')
# --------- 读取config.ini配置文件 ---------------
login_url = con.get("WebURL", "URL")

class BasePage(object):
    """基础配置"""
    def __init__(self, driver,timeout=5, poll_frequency=0.5, base_url=login_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
        self.log = Logs()

    def on_page(self):
        """
        URL地址断言
        :return: URL地址
        """
        return self.driver.current_url == self.base_url

    def _open(self, url):
        """
        打开浏览器URL访问
        :param url: URL地址
        :return:
        """
        # url = self.base_url + url
        self.driver.get(self.base_url)
        # assert self.on_page(),'Did not land on %s' % self.base_url

    def open(self):
        """
        内部调用_open私有函数
        :return:
        """
        self._open(self.base_url)


    def find_presence_elem(self, locator):
        '''
        重写元素定位：显示等待元素出现在DOM中，但并不一定可见，存在即返回该页面元素对象
        :param locator:
        :return:
        '''
        try:
            element = self.wait.until(EC.presence_of_element_located(locator=locator))
        except TimeoutError as error:
            self.log.info('等待元素超时')
            raise error
        else:
            return element

    def find_clickable_elem(self, mark):
        '''
        重写元素定位：判断页面某个元素是否是可见且是enable的，代表可点击
        :param mark:
        :return:
        '''
        try:
            element = self.wait.until(EC.element_to_be_clickable(mark))
        except TimeoutError as error:
            self.log.info('等待元素超时')
            raise error
        else:
            return element

    def send_keys(self, locator, text):
        element = self.find_presence_elem(locator)
        sleep(0.3)
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(text)

    # def send_keys(self, loc, vaule, clear_first=True, click_first=True):
    #     try:
    #         # loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
    #         if click_first:
    #             self.find_presence_elem(loc).click()
    #         if clear_first:
    #             self.find_presence_elem(loc).clear()
    #             self.find_presence_elem(loc).send_keys(vaule)
    #     except AttributeError:
    #         self.log.error("%s 页面中未能找到 %s 元素" % (self, loc))

    def click(self, mark):
        element = self.find_clickable_elem(mark)
        element.click()

    # def actions_move_click(self, ele, mark):
    #     element = self.find_presence_elem(ele)
    #     ActionChains(self.driver).move_to_element(ele).move_to_element(element).click(element).perform()

class DataAssociation:
    """
    脚本执行中存放临时参数变量，执行完清空
    """
    pass

DA = DataAssociation()



if __name__ == '__main__':
    locator1 = (By.ID, 'kw')
    locator2 = (By.ID, 'su')
    driver = webdriver.Chrome()
    case = BasePage(driver)
    driver.get('http://www.baidu.com')


    case.send_keys(locator1, 'selenium')
    # case.actions_move_click(locator2)