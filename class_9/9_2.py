#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   9_2.py
@Time    :   2020/09/05 17:17:10
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 日历
# ch9.py
from tkinter import Tk, Button, Label, RIGHT, LEFT
from calendar import *
from time import strftime, strptime
root = Tk()
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# 创建并放置星期标签
for i in range(7):
    label = Label(root, text=days[i])
    label.grid(row=0, column=i)

    weekday, numDays = monthrange(year, month)
    week = 1
    for i in range(1, numDays+1):
        label = Label(root, text=str(i))
        label.grid(row=week, column=weekday)
        weekday += 1
        if weekday > 6:
            week += 1
            weekday = 0
root = Tk()
root.mainloop()

# from tkinter import *
# from time import *
# from calendar import *


# class Application(Frame):

#     def __init__(self, master):
#         Frame.__init__(self, master)
#         self.grid()
#         self.create_widgets()

#     def create_widgets(self):

#         days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# # create labels
#         for i in range(7):
#             label = Label(self, text=days[i])
#             label.grid(row=0, column=i)

#         weekday, numDays = calendar.monthrange(year, month)
#         week = 1
#         for i in range(1, numDays + 1):
#             button = Button(self, text=str(i))
#             button.grid(row=week, column=weekday)

#             weekday += 1
#             if weekday > 6:
#                 week += 1
#                 weekday = 0


# root = Tk()
# app = Application(root)
# root.mainloop()
