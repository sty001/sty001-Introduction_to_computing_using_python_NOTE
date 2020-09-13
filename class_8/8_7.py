#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8_7.py
@Time    :   2020/09/05 09:23:02
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 在Deck类中实现重载运算len()、repr()和==。


class Deck:
    def __len__(self):
        return len(self)

    def __repr__(self):
        return 'Deck({})'.format(self.deck)

    def __eq__(self, other):
        return self.deck == other.deck
