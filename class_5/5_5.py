#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5_5.py
@Time    :   2020/08/30 23:20:58
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#迭代短语中的单词，并累加每个单词的首字母
def acronym(phrase):
    words= phrase.split()
    res= ' '
    for w in words:
        res = res + w[0].upper()
    return res


import random

def ranstr(num):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt

salt = ranstr(6)
print (salt)

