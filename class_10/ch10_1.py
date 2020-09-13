#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch10_1.py
@Time    :   2020/09/10 22:09:12
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 扫描函数scan()
import os


def scan(pathname, signatures):
    if os.path.isfile(pathname):
        infile = open(pathname)
        content = infile.read()
        infile.close()

        for virus in signatures:
            if content.find(signatures[virus]) >= 0:
                print('{},found virus {}'.format(pathname, virus))
                return
        for iyem in os.listdir(pathname):
            fullpath = os.path.join(pathname, item)
            scan(fullpath, signatures)
