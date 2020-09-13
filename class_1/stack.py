#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stack.py
@Time    :   2020/08/29 09:27:24
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

def h(n):
    print ('Start h')
    print (1/n)          # 1/2
    print (n)            # n=2

def g(n):
    print ('Start g')
    h(n-1)              #h(2)
    print (n)           # n=3
def f(n):
    print('Start f')
    g(n-1)             #g(3)
    print (n)          # n=4

f(4)