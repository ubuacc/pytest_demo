#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/1/25 16:19
import os

def new_report(testreport):
    """
    生成最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    # 列举testreport目录下的所有文件（名），结果以列表形式返回
    lists = os.listdir(testreport)
    # sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    file_new = os.path.join(testreport, lists[-1])
    return file_new