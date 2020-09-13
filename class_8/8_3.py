#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8_3.py
@Time    :   2020/09/05 00:00:05
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 实现表示矩形的类rectangle,类支持的方法：
# steSize(width,length):带两个输入参数，设置矩形的宽度和长度
# perimeter()：返回矩形的周长
# area()：返回矩形的面积


class Rectangle:
    def setSize(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord

    def perimeter(self):
        print(2*(self.x+self.y))

    def ares(self):
        print(self.x*self.y)


x = float(input('请输入矩形的长： '))
y = float(input('请输入矩形的宽： '))
C = Rectangle(x, y)
