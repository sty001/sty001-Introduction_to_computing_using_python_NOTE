#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3_12.py
@Time    :   2020/08/26 21:13:48
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#迭代列表中所有数值，检测是否有负数，并输出数值

def negatives(lst):
    for i in lst:
        if i < 0:
            print(i)
            
