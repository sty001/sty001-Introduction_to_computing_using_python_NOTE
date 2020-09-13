#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch9.py
@Time    :   2020/09/10 18:04:03
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


from tkinter import Tk, Button, Entry, Label, END
from time import strftime, strptime
from time import strftime, localtime
from tkinter.messagebox import showinfo
from tkinter import Button, Frame, Tk
from click import *


class ClickIt(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        button = Button(self, text='Click it', command=self.clicked)
        button.pack()


def clicked():  # 打印日期和时间信息
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',
                    localtime())  # 设置时间和对应格式，调用本地之间作为输出
    showinfo(message=time)  # 通过GUI窗口显示获取到的具体时间


def comput():
    global dateEnt
    date = dateEnt.get()
    weekday = serftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} was a {}'.format(date, weekday))
    dateEnt.delete(0, END)


class Day(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        label = Label(self, text='Enter date')
        label.grid(row=0, column=0)
        self.dateEnt = Entry(self)
        self.dateEnt.grid(row=0, column=1)
        button = Button(self, text='Enter', command=self.compute)
        button.grid(row=1, column=0, columnspan=2)

    def compute(self):
        date = self.dateEnt.get()
        weekday = strftime('%A', strptime(date, '%b %d, %Y'))
        showinfo(message='{} was a {}'.format(date, weekday))
        self.dateEnt.delete(0, END)


root = Tk()
day = Day(root)
clickit = clickIt(root)
clickit.pack()
root.mainloop()
