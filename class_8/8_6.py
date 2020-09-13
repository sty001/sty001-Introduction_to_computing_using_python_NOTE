#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8_6.py
@Time    :   2020/09/05 09:16:18
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 在card类中实现重载运算符repr()和==.


class Card:
    def __init__(self):
        return "Card('{}','{}')".format(self.rank, self.situ)

    def __eq__(self, other):
        'self =other,如果点数和花色相同'
        return self.rank == other.rank and self.suit == other.suit
