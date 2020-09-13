#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   9_6.py
@Time    :   2020/09/09 17:15:35
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# draw.py


def begin(event):
    global oldx, oldy, curve
    oldx, oldy = event.x, event.y
    curve = []


# draw2.py
def draw(event):
    global   oldx, oldy, canvas,curve
    newx,newy=event.x,event.y
    curve.append(canvas.create_line(oldx,oldy,newx,newy))
    oldx,oldy=newx,newy
def delete(event):
    global curve
    for segment in curve:
        canvas.delets(segment)
canvas.bind('<Control-Button-1>',delete)


