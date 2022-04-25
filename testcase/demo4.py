#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/4/24 10:01

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class demo4():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, timeout=5, poll_frequency=0.5)
        self.driver.get('https://cloud-uat.anker-in.com')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def find_presence_elem(self, locator):
        '''
        重写元素定位：显示等待元素出现在DOM中，但并不一定可见，存在即返回该页面元素对象
        :param locator:
        :return:
        '''
        try:
            element = self.wait.until(EC.presence_of_element_located(locator=locator))
        except TimeoutError as error:
            # self.log.info('等待元素超时')
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
            # self.log.info('等待元素超时')
            raise error
        else:
            return element

    def scroll(self):
        self.driver.execute_script(""" 
            (function () { 
                var y = document.body.scrollTop; 
                var step = 100; 
                window.scroll(0, y); 
                function f() { 
                    if (y < document.body.scrollHeight) { 
                        y += step; 
                        window.scroll(0, y); 
                        setTimeout(f, 50); 
                    }
                    else { 
                        window.scroll(0, y); 
                        document.title += "scroll-done"; 
                    } 
                } 
                setTimeout(f, 1000); 
            })(); 
            """)

    def test_demo(self):

        # 切换电脑登录方式
        self.find_clickable_elem((By.XPATH, '//*[@id="tabA11"]')).click()
        # 用户登录
        self.find_presence_elem((By.ID, 'j_username')).send_keys('luke.ren')
        self.find_presence_elem((By.ID, 'j_password')).send_keys('Ni&Li123')
        self.find_clickable_elem((By.ID, 'loginButton')).click()
        # 进入测试页面
        self.find_clickable_elem((By.XPATH, '//*[@id="menu"]/li[1]/div/span/span')).click()
        self.find_clickable_elem((By.XPATH, '//*[@id="menu"]/li[1]/ul/li[7]/a')).click()
        #点击新增按钮
        self.find_clickable_elem((By.XPATH, '//*[@id="add"]/div/button')).click()
        sleep(3)
        self.find_clickable_elem((By.CSS_SELECTOR, 'form.container.ant-form.ant-form-inline.nowrap-label > div.container-box.box-content > form.container.ant-form.ant-form-inline.eq-width > div[id="forecast_unit_id"] > div > div.ant-col.ant-form-item-control-wrapper > div > span > div > div > div.ant-select-selection__rendered > div.ant-select-selection__placeholder')).click()
        self.find_presence_elem((By.CSS_SELECTOR, 'div[id="forecast_unit_id"] > div > div.ant-col.ant-form-item-control-wrapper > div > span > div > div > div > div.ant-select-search.ant-select-search--inline > div > input')).send_keys('US_AMAZON')
        sleep(2)
        self.find_clickable_elem((By.CSS_SELECTOR, 'div.ant-select-dropdown-content > ul > li')).click()
        sleep(2)
        self.find_clickable_elem((By.CSS_SELECTOR, 'div[id="type"] > div > div.ant-col.ant-form-item-control-wrapper > div > span > div > div > div > div')).click()
        self.find_clickable_elem((By.CSS_SELECTOR, 'div.ant-select-dropdown.ant-select-dropdown--single.ant-select-dropdown-placement-bottomLeft > div.ant-select-dropdown-content > ul > li.ant-select-dropdown-menu-item.ant-select-dropdown-menu-item-active')).click()
        self.find_presence_elem((By.XPATH, '//*[@id="other_requirements"]/div/div[2]/div/span/input')).send_keys('5')
        sleep(3)
        # 选择SKU
        self.find_clickable_elem((By.CSS_SELECTOR, 'div[id="c_operation_sm_plan_order_item"] > div > div > div > div > div > div.ant-table-scroll > div > table > tbody > tr > td:nth-child(2) > div > div > div > div > span > div > div > div > div.ant-select-selection__placeholder')).click()
        sleep(1)
        self.find_presence_elem((By.CSS_SELECTOR, 'div[id="c_operation_sm_plan_order_item"] > div > div > div > div > div > div.ant-table-scroll > div > table > tbody > tr > td:nth-child(2) > div > div > div > div > span > div > div > div > div.ant-select-search.ant-select-search--inline > div > input')).send_keys('A8633022')
        sleep(5)
        self.find_clickable_elem((By.CSS_SELECTOR, 'div.ant-select-dropdown-content > ul > li.ant-select-dropdown-menu-item.ant-select-dropdown-menu-item-active')).click()
        sleep(2)
        self.find_presence_elem((By.CSS_SELECTOR, 'div[id="c_operation_sm_plan_order_item"] > div > div > div > div > div > div.ant-table-scroll > div > table > tbody > tr > td:nth-child(6) > div > div > div > div > span > input')).send_keys('99')
        sleep(1)
        # js = "var q=document.documentElement.scrollTop=10000"
        # self.driver.execute_script(js)

        # 页面跳到指定位置
        target = self.driver.find_element(By.CSS_SELECTOR, "div[id='c_operation_sm_plan_order_item'] > div > div > div > div > div > div.ant-table-scroll > div > table > tbody > tr > td:nth-child(6) > div > div > div > div > span > input")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        sleep(1)
        # 选择渠道CRD
        self.find_clickable_elem((By.CSS_SELECTOR, 'div[id="channel_claim_arrival_date"] > div > div.ant-col.ant-form-item-control-wrapper > div > span > span > span > div > input')).click()
        self.find_clickable_elem((By.CSS_SELECTOR, 'body > div:nth-child(15) > div > div > div > div > div.ant-calendar-date-panel > div.ant-calendar-footer > span > a')).click()
        # 选择物流方式
        self.find_clickable_elem((By.CSS_SELECTOR, 'form.container.ant-form.ant-form-inline.nowrap-label > div[id="shipping_way"] > div > div.ant-col.ant-form-item-control-wrapper > div > span > div > div > div > div')).click()
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).click()
        self.find_clickable_elem((By.XPATH, '//*[@class="ant-select-dropdown-content"]/ul/li[6]')).click()
        sleep(2)
        # 点击新增保存按钮
        self.find_clickable_elem((By.XPATH, '//*[@id="save"]/div/button')).click()

if __name__ == '__main__':
    run = demo4()
    run.test_demo()


