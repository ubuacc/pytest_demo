#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/4/6 15:31
from demo import da
from demo1 import aaaac

class bbbbc():
    def bc(self):
        aaaac().ac()
        print(hasattr(da, 'data'))
        print(getattr(da, 'data'))
        print('1')
        setattr(da, 'test', 2)

# bbbbc().bc()
from public.page.basepage import DA
from page.mdp_login import Login
from public.models.getdriver import browser
import logger
from page.mdp_ipc_channel import MarketChannel
class fe():
    def ddd(self):
        log = logger.Logs()
        username = 'david.luo'
        password = 'Ni&Li12345'
        driver = browser()
        case = Login(driver)
        case.login_user(username, password)
        case2 = MarketChannel(driver)

        case2.open_marketchannel()
        case2.add_marketchannel("test146", "测试11", "test11", "1111111111")
        print(id(DA))
        print(getattr(DA, 'mc_number'))
        case2.demo()

fe().ddd()


