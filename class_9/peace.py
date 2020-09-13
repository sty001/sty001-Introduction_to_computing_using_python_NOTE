#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   peace.py
@Time    :   2020/09/05 15:53:24
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM, Label, PhotoImage
root = Tk()
photo = PhotoImage(
    file='F:\code_homework\Introduction_to_computing_using_python_NOTE\class_9\peace.gif')
peace = Label(master=root,
              image=photo,
              width=300,
              height=180)
peace.pack()
root.mainloop()
