#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   scope3.py
@Time    :   2020/08/29 09:24:01
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
def f(b):
    global a
    a= 6
    return a*b

a=0
print ('f(3)={}'.format(f(3)))
print ('a is {}'.format(a))
