#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   9_7.py
@Time    :   2020/09/10 14:54:32
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
def down():
  global y,canvas
  canvas.create_line(x,y,x,y+10)
  y+=10
def left():
  global x, canvas
  canvas.create_line(x,y,x-10,y)
  x-=10
def reght():
  global x, canvas
  canvas.create_line(x,y,x+10,y)
  x+=10