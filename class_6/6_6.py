#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6_6.py
@Time    :   2020/09/03 22:57:39
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#获取列表中出现的所有集合的并集
def sync(phonebooks):
    res=set()
    for phonebook in phonebooks:
        res =res | phonebook
    return res
    