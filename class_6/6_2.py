#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6_2.py
@Time    :   2020/09/03 21:09:25
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#实现函数 rlookup(),提供电话簿的反向查找，函数带一个表示电话的字典作为输入参数，

def rlookup(phonebook):
    while True:
        number=input('Enter phone number in the format (xxx)xxx-xx-xx: ')
        if number in phonebook:
            print(phonebook[number])
        else:
            print('The number you entered is not in use.')