#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3_9.py
@Time    :   2020/08/26 21:00:44
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#实现函数average()，带两个数值作为输入参数，要求返回他们的平均值

def average (x,y):
    fun=(x+y)/2
    print(fun)


x=int(input('请输入整数 x：'))
y=int(input('请输入整数 y: '))
div = average(x,y)