#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   phone.py
@Time    :   2020/09/05 16:57:04
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 电话拨号键
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM, Label, PhotoImage, RIGHT, LEFT, RAISED
root = Tk()
labels = [['1', '2', '3'],  # 电话拨号标签文本
          ['4', '5', '6'],  # 布局为网格
          ['7', '8', '9'],
          ['*', '0', '#']]
for r in range(4):  # 对于每个行r=0，1，2，3
    for c in range(3):  # 对于每个列c=0，1，2
        label = Label(root, relief=RAISED, padx=10,
                      text=labels[r][c])  # 设置边框样式、价款标签、编辑标签文本
        label.grid(row=r, column=c)  # 将标签放置于R行C列
root.mainloop()
