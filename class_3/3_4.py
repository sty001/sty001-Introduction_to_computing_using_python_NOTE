#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3_2.py
@Time    :   2020/08/26 20:37:43
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#编写一个python语言程序，首先要求用户输入登录ID（一个字符串）。然后程序检测用户输入的ID是否位于表示有效用户的列表['joe','sue','hani','sophie']中，如果用户是有效用户，则输出适当的提示信息。无论用户是否有效，均在输出'Done'后结束执行。

users=['joe','sue','hani','sophie']
id = input ('Login: ')
if id in users:
    print ('You are in!')
else:
    print ('User unknown.')
print('Done.')
