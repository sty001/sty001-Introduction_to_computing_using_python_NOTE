#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   twoway.py
@Time    :   2020/08/26 19:45:30
@Author  :   STY_lcmg 
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
temp=eval(input('Enter the current temperature: '))

if temp > 86:
    print('It is hot!')                           #当输入小于等于86的时候，不会打印if选择语句下的print内容，直接输出后面print内的Goodbey
    print('Be sure to drink liquids.')
    
else:
    print('It is not hot.')
    print('Bring a jacket.')
print('Goodbye!')