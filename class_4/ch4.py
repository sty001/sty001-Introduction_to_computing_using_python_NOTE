#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch4.py
@Time    :   2020/08/27 13:50:52
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
def griwthrates(n):
    print('i    i**2     i**3   2**i')
    formatStr='{0:2d} {1:6d} {2:6d} {3:6d}'
    for i in range(2,n+1):                                          #这种输出矩阵的 之间的距离是个问题  还需改进使其美观
        print(formatStr.format(i, i**2, i**3, 2**i,sep='    '))

n=input('Enter a inter number: ')
fun=griwthrates(int(n))
