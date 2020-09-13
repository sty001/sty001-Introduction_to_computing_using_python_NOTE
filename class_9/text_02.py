#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   text_02.py
@Time    :   2020/09/10 19:57:53
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


from tkinter import *


class MainWindow:
    def __init__(self):
        self.frame = Tk()

        self.label_name = Label(self.frame, text="name:")
        self.label_age = Label(self.frame, text="age:")
        self.label_sex = Label(self.frame, text="sex:")

        self.text_name = Text(self.frame, height="1", width=30)
        self.text_age = Text(self.frame, height="1", width=30)
        self.text_sex = Text(self.frame, height="1", width=30)

        self.label_name.grid(row=0, column=0)
        self.label_age.grid(row=1, column=0)
        self.label_sex.grid(row=2, column=0)

        self.button_ok = Button(self.frame, text="ok", width=10)
        self.button_cancel = Button(self.frame, text="cancel", width=10)

        self.text_name.grid(row=0, column=1)
        self.text_age.grid(row=1, column=1)
        self.text_sex.grid(row=2, column=1)

        self.button_ok.grid(row=3, column=0)
        self.button_cancel.grid(row=3, column=1)

        self.frame.mainloop()


frame = MainWindow()
