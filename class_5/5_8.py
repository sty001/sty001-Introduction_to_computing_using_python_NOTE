#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5_8.py
@Time    :   2020/09/02 21:07:40
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#连续比较数列中相邻两项的大小  最终实现按从大到小的顺序排列

def bubbleesort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):                #每一次交换的过程都会展现
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                print (lst)

str=input('以空格为间隔连续输入一个数组：')
lst=[int(j) for j in str.split()] 
List=bubbleesort(lst)
