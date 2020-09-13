#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5_3.py
@Time    :   2020/08/30 22:33:18
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#检查相邻列表之间是否相等

def arithmetic(lst):
    if len(lst) <2 :
        return True
    diff = lst[1]-lst[0]
    for i in range(1,len(lst)-1):
        if lst[i+1]-lst[i] !=diff:
            return False
    return True

