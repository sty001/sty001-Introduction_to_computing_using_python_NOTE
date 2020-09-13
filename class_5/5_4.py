#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5_4.py
@Time    :   2020/08/30 23:14:41
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#累成器 
def factorial(n):
    res = 1
    for i in range(2,n+1):
        res *= i

        print (res)
    

number= factorial(int(input('Enter a number: ')))