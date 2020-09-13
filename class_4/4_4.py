#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4_4.py
@Time    :   2020/08/26 22:52:46
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
def even(n):
    for i in range(2,n+1):
        if i%2==0 or i%3==0:
            print (i,end=',')

even(int(input('请输入你要求的能被2和3整除的数的范围： ')))
