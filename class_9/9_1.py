#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   9_1.py
@Time    :   2020/09/05 16:39:58
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM, Label, PhotoImage, RIGHT, LEFT
root = Tk()
label1 = Label(root, text='Peace & Love', background='black', width=20,
               height=5, foreground='white', font=('Helvetica', 18, 'italic'))
label1.pack(side=LEFT)
photo = PhotoImage(
    file='F:\code_homework\Introduction_to_computing_using_python_NOTE\class_9\peace.gif')
label2 = Label(root, image=photo)
label2.pack(side=RIGHT, expand=True, fill=BOTH)
root.mainloop()
