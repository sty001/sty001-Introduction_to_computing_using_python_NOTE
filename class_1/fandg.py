#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fandg.py
@Time    :   2020/08/29 09:09:16
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

def f(y):
    x= 2
    return g(x)

def g(y):
    global x
    x=4
    return x*y

x=0
res=f(x)
print ('x={},f(0)={}'.format(x,res))