#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5_10.py
@Time    :   2020/09/02 22:52:11
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#编写一个函数interest(),带一个浮点数利率作为输入参数，函数计算并返回一笔投资价值翻倍所需的时间。
def interest(rate):
    amount = 100
    count = 0
    while amount < 200:
        count +=1
        amount += amount*rate
        if amount >= 200:
            print ('投资价值翻倍需要  '+ str(count) +' 年')
            print ('本金及盈利总数为： '+str(amount)+'  元')
    return count

rate_1=float(input('请输入投资利率: '))
r=interest(rate_1)