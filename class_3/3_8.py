#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3_8.py
@Time    :   2020/08/26 20:54:23
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#在交互式命令行中直接定义一个函数perimeter(),带一个输入参数--圆半径，要求返回圆的周长。

import math
def perimeter(radius):
    return 2*math.pi*radius
    
radius=float(input('Enter a number make radius: '))
S=perimeter(radius)
print  (S)    

