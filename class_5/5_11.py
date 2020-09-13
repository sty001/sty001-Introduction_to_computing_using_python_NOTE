#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5_11.py
@Time    :   2020/09/02 23:18:04
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#计算 e 的精确值
import math

def approxE(error):
    prev = 1
    current = 2
    i = 2 
    while current-prev > error:
        prev = current
        current = prev + 1/math.factorial(i)
        i += 1
    print (current)    #放在while 循环外面，直接输出最后的近似结果 不用显示每次的遍历求解过程的结果
    return current
error=float(input('请输入你想精确到的误差范围： '))
e=approxE(error)