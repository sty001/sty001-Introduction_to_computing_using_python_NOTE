#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   9_8.py
@Time    :   2020/09/10 15:09:49
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
from tkinter import Text, Frame, BOTH


class KeyLogger(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self > pack()
        tezt = Text(width=20, height=5)
        text.bind('<KeyPress>', self.record)
        text.pack(expand=True, file=BOTH)

    def record(self, event):
        print('char={}'.format(event, keysym))
