#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4_9.py
@Time    :   2020/08/28 23:14:15
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#移除文本中的标点符号，并把每一个标点符号换成一个空字符

def words(filename):
    infile=open(filename,'r')
    content = infile.read()
    infile.close()
    table =str.maketrans('!,.:;?',6*' ')
    content=content.translate(table)
    content=content.lower()
    return content.split()

    