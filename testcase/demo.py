
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/1/6 17:31
import os

from public.models.getyaml import YamlRead

filepath = os.path.abspath(os.path.join(os.getcwd(), '../..'))+os.sep+'testdata'+os.sep+'testdata_login.yaml'
print(filepath)
testdata = YamlRead('testdata', 'testdata_login.yaml').yaml_all()
print(testdata)