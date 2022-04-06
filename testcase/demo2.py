#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/4/6 15:31
from demo1 import da, ac

def bc():
    ac()
    print(getattr(da, 'data'))
    print('1')
    setattr(da, 'test', 2)



