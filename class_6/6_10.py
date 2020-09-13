#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6_10.py
@Time    :   2020/09/04 20:43:17
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#通过单位圆和边长为2的正方形来求解π
import random
def approxPi(total):
    count =0
    for i in range(total):

        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        if x**2+y**2<=1:
            count +=1
    print (4*count/total)

#n为模拟随机投掷飞镖中靶的数量
total=int(input('请输入成功投中把子的次数： '))
pi=approxPi(total)