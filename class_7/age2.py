#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   age2.py
@Time    :   2020/09/04 21:37:13
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#捕获和异常处理函数
try:
    intAge=int(input('Enter your age: '))
    print('you are {} years old.'.format(intAge))
except:
    print('Enter your age using digits 0-9!')
    
