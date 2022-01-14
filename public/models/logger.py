#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time:  10:10
import logging
import logging.handlers
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import time
from config import setting

# 日志存放文件夹，如不存在，则自动创建一个logs目录
if not os.path.exists(setting.LOG_DIR):os.mkdir(setting.LOG_DIR)

class Logs(object):
    def __init__(self):
        self.logger = logging.getLogger("")
        # 设置输出的等级
        LEVELS = {'NOSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}
        # # 创建文件目录
        # projectpath = os.path.abspath(os.path.join(os.getcwd(), '../..'))
        # logs_dir = projectpath+os.sep+"logs"
        # if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
        #     pass
        # else:
        #     os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        logfilename = '%s.txt' % timestamp
        logfilepath = os.path.join(setting.LOG_DIR, logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5)
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)