#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Card.py
@Time    :   2020/08/30 16:24:35
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

class Card:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def gitRank(self):
        return self.rank

    def gitSuit(self):
        return self.suit

# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

# import random

# list = [20, 16, 10, 5]
# random.shuffle(list)
# print ('随机排序列表 :', list)

# random.shuffle(list)                      #shuffle() 所有元素随机排列
# print ('随机排序列表 : ',  list)