#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/08/29 09:48:43
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
import random

list_1 = []

#生成20位随机整数列表

for i in range(20):

    list_1.append(random.randint(0,100))

    print(list_1)

    #统计新生成的整数在列表中的数量

    if list_1.count(list_1[i]) > 1:

        #判断生成的是否为最后一个元素

        if i < (20-1):

            print('移除了一个重复元素：',list_1[i])

            #移除重复整数元素

            list_1.pop(i)

            #移除后补加一个随机整数元素

            list_1.append(random.randint(0,100))   

        #移除最后一个重复元素

        else:

            #反复确认移除后生成的元素不再重复

            while True:

                if list_1.count(list_1[i]) > 1:

                    print('移除了最后一个重复元素：',list_1[i])

                    list_1.pop(i)

                    list_1.append(random.randint(0,100))

                else:

                    print(list_1)

                    break