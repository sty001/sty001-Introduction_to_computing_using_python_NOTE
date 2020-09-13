#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6_5.py
@Time    :   2020/09/03 22:43:52
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#实现正向电话簿查询应用程序，函数带一个表示电话簿的字典作为输入参数
def lookup(phonebook):
    while True:
        first = input ('Enter the first name: ')
        last = input('Enter the last name: ')
        person = (first,last)
        if penson in phonebook:
            print(phonebook[person])
        else:
            print('The name you entered is not known.')