#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   for.py
@Time    :   2020/08/26 19:52:16
@Author  :   STY_lcmg 
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
phrase=input('Enter a phrase: ')
for c in phrase:
    if c in 'aeoiuAEIOU':
        print(c)
        print('您输入的'+c+'是元音字母!')
    else:
        print('您输入的'+c+'不是元音字母！')