# -*- coding:utf-8
"""
@author:liucunhu
@contact:786608954@qq.com
@version:1.0.0
@file:test.py
@time:2022/3/27  18 38

"""
import re
rstrs='/umanage/permissionedit/4'
pattern=r'/umanage/permissionedit/(\d+)/'
print(re.match(pattern,rstrs))