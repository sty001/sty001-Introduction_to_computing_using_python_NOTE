#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8_4.py
@Time    :   2020/09/05 00:00:55
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#添加一个__init__()方法到勒种，包括输入参数species和language的默认值
def __init__(self,cardList=None):
  if cardList != None:
    self.deck = cardList
  else:
    self.deck