#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5_9.py
@Time    :   2020/09/02 21:18:04
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#使用嵌套循环 产生所有的列和行索引对  行列式 矩阵

def add2D(t1,t2):
    nrows=len(t1)                     #计算行数和列数   数列下角标
    ncols=len(t1[0])
    for i in range(nrows):              
        for j in range(ncols):
            t1[i][j]+=t2[i][j]

str=input('以空格为间隔连续输入一个数组：')
lst=[int(j) for j in str.split()] 
array = [[0]*n for i in ]
        

