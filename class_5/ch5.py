#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch5.py
@Time    :   2020/08/28 23:23:34
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#条件选择语句
def temperature(t):
    if t>86:
        print ('It is hot!')
    elif t>32:
        print ('It is cool.')
    else:
        print('It is freezing!')


number=temperature(int(input('Enter a number: ')))

#ch5.py List 降序排列
# import random

# def sorted(lst):
#     for i in range(0,len(lst-1)):
#     # for i in range(0,len(lst)-1):
#         if lst[i]>lst[i+1]:
#             return False           
#     return True
# list=[]
# list=list.append(print(random.sample(range(1,100),10)))      #还没想好怎么调用自动生成的随机数，待更新
# List=sorted(list)


#P125 ch5.py   斐波那契数
# def fibonacci(bound):
#     precious = 1
#     current = 1
#     while current <= bound:
#         precious,current = current,precious+current
#     return current
