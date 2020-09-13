#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   clickit.py
@Time    :   2020/09/05 17:27:58
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
from tkinter import Tk, Button
from tkinter.messagebox import showinfo
from time import strftime, localtime


def clickied():  # 打印日期和时间信息
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',
                    localtime())  # 设置时间和对应格式，调用本地之间作为输出
    showinfo(message=time)  # 通过GUI窗口显示获取到的具体时间


root = Tk()
# 创建标有'Clicked it '文字的按钮以及clicked时间处理函数
button = Button(root, text='Click it', command=clickied)
button.pack()  # 单击按钮时间处理程序，
root.mainloop()
