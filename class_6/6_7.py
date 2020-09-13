#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6_7.py
@Time    :   2020/09/03 23:00:25
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

def encoding(text):
    print('Char Decimal Hex Binary')
    for c in text:
        code = ord(c)
        print('{}   {:7}  {:4x} {:7b}'.format(c,code,code,code))