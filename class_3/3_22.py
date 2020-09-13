#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3_22.py
@Time    :   2020/08/26 21:50:56
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
import math
numList=[2,3,4,5,6,7,8,9]
even=[i for i  in  numList  if (i**2)%8==0]   #输出列表元素平方能被8整除的数值
print (even)
even1=[i for i  in  numList  if (i**2)%4==0 or (i**2)%8==0]            #输出列表元素平方能被8或者被4整除的数值
print (even1)