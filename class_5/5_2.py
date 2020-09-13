#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5_2.py
@Time    :   2020/08/30 22:22:40
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#计算 2 的1~n次幂
def powers(n):
    for i in range(1,n+1):
        print (2**i, end=' ')

num2= powers(int(input('请输入你需要求的次幂数： ')))
