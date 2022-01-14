#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/1/14 10:02
import unittest
import unittest
from .driver import browser

class TestUnit(unittest.TestCase):
    '''
    自定义TestUnit类
    '''
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

