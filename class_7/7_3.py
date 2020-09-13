#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   7_3.py
@Time    :   2020/09/04 21:57:20
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#为open()函数创建爱你一个“包装器”函数safe-open()，调用open()来打开一个在当前工作目录不存在的文件时，会抛出一个异常
def safe_open(filename,mode):
    try:
        infile=open(filename,mode)
        return infile
    except:
        return None


