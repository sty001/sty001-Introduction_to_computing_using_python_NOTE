#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   smileyPeace.py
@Time    :   2020/09/05 15:27:02
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT, RIDGE
root = Tk()
text = Label(root,
             font=('Helvetica', 16, 'bold italic'),
             foreground='white',
             background='black',
             padx=25,
             pady=10,
             text='Peace with a smile.')
text.pack(side=BOTTOM)
peace = PhotoImage(
    file='F:\code_homework\Introduction_to_computing_using_python_NOTE\class_9\peace.gif')  # 注意 此处地址根据自己的实际情况进行修改
peaceLabel = Label(root,
                   borderwidth=3,
                   relief=RIDGE,
                   image=peace)
peaceLabel.pack(side=LEFT)
smiley = PhotoImage(
    file='F:\code_homework\Introduction_to_computing_using_python_NOTE\class_9\smiley.gif')  # 注意 此处地址根据自己的实际情况进行修改
smileyLabel = Label(root,
                    image=smiley)
smileyLabel.pack(side=RIGHT)
root.mainloop()
