#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   9_4.py
@Time    :   2020/09/09 16:38:28
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


from tkinter import *
from time import *
from calendar import *


def compute():
    global dateEnt
    date = dateEnt.get()
    weekday = strftime()
    dateEnt.insert(0, weekday+' ')


def clear():
    global dateEnt
    dateEnt.delete(0, END)
    button = Button(root, text="Enter", command=compute)
    button.grid(row=1, column=0)

    button = Button(root, text="Clear", command=compute)
    button.grid(row=1, column=1)
