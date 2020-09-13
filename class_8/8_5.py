#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8_5.py
@Time    :   2020/09/05 09:06:19
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 修改类Deck的构造函数，使得该类可以用于非标准52张扑克牌的扑克牌游戏。
# 允许构造函数不带参数或者带一个扑克牌列表参数，故而需要实现函数__init__()，带一个有默认值得参数，这个默认值实际上是包含52张扑克牌的列表，但是它并没有直接创建这个列表。


def _init__(self, cardList=None):
    if cardList != None:  # 提供了输入扑克牌列表
        self.deck = cardList
    else:
        pass  # 没有提供输入扑克牌列表
        # self.deck是一个标准的52张扑克牌列表
