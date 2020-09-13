#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6_8.py
@Time    :   2020/09/03 23:04:09
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

def char(low,high):                     #打印ASCII嘛位于low,high之间的数
    for i in range(low,high+1):         #打印整数ASCII码及对应字符
        print('{}: {}'.format(i,chr(i)))
