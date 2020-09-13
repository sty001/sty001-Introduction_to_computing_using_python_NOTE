#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dynamic.py
@Time    :   2020/08/26 20:16:41
@Author  :   STY_lcmg 
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
s = input('Enter square or cube: ')     #用户输入cube，则被定义为立方函数;如果输入square，则被定义为平方函数
if s == 'square':
    def f(x):
        return x*x

else:
    def f(x):
        return x**3
