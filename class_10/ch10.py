#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch10.py
@Time    :   2020/09/10 21:31:58
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 第十章节 递归


from turtle import Screen, Turtle


def countdown(n):
    if n <= 0:  # 终止条件 防止无限递归
        print('Blastoff!!!')
    else:
        print(n)
        countdown(n-1)


def vertical(n):
    if n < 10:
        print(n)
    else:
        vertical(n//10)
        print(n % 10)

# ch10.py pattern()函数


def pattern(n):  # 不建议要输过大的数，
    if n == 0:
        print(0, end=' ')
    else:
        pattern(n-1)
        print(n, end=' ')
        pattern(n-1)
# 函数koch()


def koch(n):
    if n == 0:
        return 'F'
    tmp = koch(n-1)
    return tmp+'L'+tmp+'R'+tmp+'L'+tmp


# 使用koch()绘制 科赫曲线


def drawKoch(n):  # 建议不要输太大的数，绘图速度太慢了，待改进中
    s = Screen()
    t = Turtle()
    directions = koch(n)
    for move in directions:
        if move == 'F':
            t.forward(300/3**n)
        if move == 'L':
            t.lt(60)
        if move == 'R':
            t.rt(120)
    s.bye()


n1 = int(input('Enter a int number: '))
number = countdown(n1)
number = vertical(n1)
number = pattern(n1)
number = koch(n1)
number = drawKoch(n1)
