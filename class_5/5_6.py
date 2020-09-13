#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5_6.py
@Time    :   2020/08/31 00:10:39
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#输出正因子列表
def divisors(n):
    res = []
    for i in range(1,n+1):
        if n % i ==0:
            res.append(i)
            print (res)
    return res

    
number=divisors(int(input('Enter a int number: ')))
