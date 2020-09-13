#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   9_3.py
@Time    :   2020/09/05 17:42:02
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
from tkinter import Tk,  Button, Label, RIGHT, LEFT
from tkinter.messagebox import showinfo
from time import strftime, strptime
root = Tk()


def greenwich():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S  %p\n', gmtime())
    print('Greenwich time\n' + time)


def local():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S  %p\n', localtime())
    print('Local time\n' + time)


buttonl = Button(root, text='Local time', command=local)
buttonl.pack(side=LEFT)
buttong = Button(root, text='Greenwich time', command=greenwich)
buttong.pack(side=RIGHT)
