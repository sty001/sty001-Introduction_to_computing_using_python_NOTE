#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4_10.py
@Time    :   2020/08/28 23:19:53
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#迭代文件各行
def myGrep(filename,terget):
    infile =open(filename)
    for line in infile:
        if terget in line:
            print (line, end=' ')
            