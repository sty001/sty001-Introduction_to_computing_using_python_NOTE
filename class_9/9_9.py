#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   9_9.py
@Time    :   2020/09/10 17:59:18
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# ch9.py

b = Button(buttons, text='up', command=self.up)
b.grid(row=0, column=0, columnspan=2)


def up(self):
    self.cancas.create_line(self.x, self.y, self.x, self.y-10)
    self.y -= 10
