#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6_1.py
@Time    :   2020/09/03 18:48:24
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#编写一个函数birthState()，带 一个最近几届美国总统的姓名作为出入参数，返回该总统的出生所在州

def birthState(president):
    states={'Barack Hussein Obama II': 'Hawaii',
            'George Walker Bush': 'Connecticut',
            'Wikkiam Jefferson Clinton':'Arkansas',
            'George Herbert Walker Bush':'Massachusswtts',
            'Ronald Wilson Reagan':'Illinois',
            'James Earl Carter,Jr':'Georgia'}

    return states[president]




