#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8_8.py
@Time    :   2020/09/04 23:57:20
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 实现类Queue的方法dequeue()，从一个空队列引发一个keyboarInterrupt异常.


class Vector(Point):
    def __mul__(self, v):
        return self.x*v.x+self.y*v.y

    def __add__(self, v):
        return Vector(self.x+V.x, self.y+v.y)

    def __repr__(self):
        return 'Vector{}'.format(self.get())
