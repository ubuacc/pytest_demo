#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/1/14 15:35
from selenium.webdriver import Remote

def browser():
    """
    启动浏览器驱动
    :return: 返回浏览器驱动URL
    """
    try:
        host = '127.0.0.1:4444'
        driver = Remote(command_executor='http://' + host + '/wd/hub',
                        desired_capabilities={ 'platform': 'ANY',
                                               'browserName': 'chrome',
                                               'version': "",
                                               'javascriptEnabled': True
                                            }
                        )
        return driver
    except Exception as msg:
        print("驱动异常-> {0}".format(msg))

