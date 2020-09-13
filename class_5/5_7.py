#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5_7.py
@Time    :   2020/08/31 20:26:53
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

# def sum():
#     sum= a+b
#     print (sum)

# a=int(input('请输入数值a： '))
# b=int(input('请输入数值b:  '))
# sum = sum()         


#使用嵌套循环模式 将第一个列表中的每个整数乘以第二个列表中的整数，外部for循环遍历第一个列表，内部for循环遍历第二个列表
def xumlt(l1,l2):
    l=[]
    for i in l1:
        for j in l2:
            l.append(i*j)
            print (l)

    return

str1=input('以空格为间隔连续输入一个数组：')
str2=input('以空格为间隔连续输入一个数组：')
l1=[int(i) for i in str1.split()] 
l2=[int(j) for j in str2.split()] 
xuml=xumlt(l1,l2)