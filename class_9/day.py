#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   day.py
@Time    :   2020/09/07 19:03:06
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


from tkinter.messagebox import showinfo
from time import strftime, strptime
from tkinter import Tk, Button, Entry, Label, END


def compute():  # 定义compute
    global dateEnt
    date = dateEnt.get()
    # 注意输入的时候 月份在前(英语书写) 然后日期 最后年份 中间不要逗号
    weekday = strftime('%A', strptime(date, '%b %d %Y'))
    showinfo(message='{} was a {}'.format(date, weekday))
    dateEnt.delete(0, END)


root = Tk()
label = Label(root, text='Enter date')
label.grid(row=0, column=0)
dateEnt = Entry(root)
dateEnt.grid(row=0, column=1)
# 需先对compute进行定义，再调用，否则会报错，书本中定义部分在后，之前主干部门在前 但是说能正常执行显示，暂不明
button = Button(root, text='Enter', command=compute)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()
