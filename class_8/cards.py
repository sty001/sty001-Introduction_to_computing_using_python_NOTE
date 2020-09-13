#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   cards.py
@Time    :   2020/08/30 16:44:18
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

from random import shuffle
class Deck:
    ranks={'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    suit ={'\u2660','\u2661','\u2662','\u2663'}

    def __init__(self):                             #初始化52张扑克牌的一副牌
        self.deck =[]                               #Deck初始化为空
        for suit in Deck.suit:
            for rank in Deck.ranks:                 #指定rank和suit是Deck类变量
                self.deck.append(Card(rank,suit))
    def dealCard(self):                             #从一副牌的顶部发牌
        return self.deck.pop()

    def shuffle(self):                              #'洗牌'
        shuffle(self.deck)


