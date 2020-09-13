#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10_5.py
@Time    :   2020/09/10 22:26:41
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


from turtle import Screen, Turtle


def koch(n):
    if n == 0:
        return 'F'
    tmp = koch(n-1)
    return tmp+'L'+tmp+'R'+tmp+'L'+tmp


def drawSnowflake(n):
    s = Screen()
    t = Turtle()
    directions = koch(n)

    for i in range(3):
        for move in directions:
            if move == 'F':
                t.fd(300/3**n)
            if move == 'L':
                t.lt(60)
            if move == 'R':
                t.rt(120)
        t.rt(120)
    s.bye()


n1 = int(input('Enter a number: '))
number = drawSnowflake(n1)
