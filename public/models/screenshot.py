#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/1/5 16:10

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config import setting

def screenshot(driver,filename):
        '''
        截图
        :param driver:
        :param filename: 截图文件名
        :return:返回指定路径的截图文件
        '''
        file_name = filename + '.png'
        filepath = os.path.join(setting.Screenshots_DIR, 'screenshots')
        screen_path = os.path.join(filepath, file_name)
        return driver.get_screenshot_as_file(screen_path)
