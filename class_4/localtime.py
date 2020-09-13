#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Newtime.py
@Time    :   2020/08/26 22:17:01
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
import time  
from datetime import datetime
localtime=time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(time.time()))
print ("本地时间为 :", localtime)