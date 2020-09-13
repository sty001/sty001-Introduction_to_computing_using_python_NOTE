#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch8.py
@Time    :   2020/09/04 22:04:03
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 类point


class Point:
    def setx(self, xcoord):
        self.x = xcoord

    def sety(self, ycoord):
        self.y = ycoord

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# 定义类Queue
class Queue:
    def __init__(self):
        self.q = []  # 实例化一个空列表

    def isEmpty(self):  # 如果队列为空，则返回Ture，否则返回False
        return (len(self.q) == 0)

    def enqueue(self, item):
        return self.q.append(item)  # 插入一个项到队列的尾部

    def dequeue(self):  # 从队列头部移除一个项并返回该项
        return self.q.pop(0)


# 类定义 重写父类的方法
class Animal:
    def setSpecties(self, species):
        self.spec = species

    def steLanguage(self, language):
        self.lang = language

    def speak(self):
        print('I am a {}  and I {}.'.format(self.spec, self.lang))


# 类的继承、替换、扩展
class Super:
    def method(self):
        print('in super.method')


class Inheritor(Super):
    pass


class Replacer(Super):
    def mathod(self):
        print('in Rep;acer.mathod')


class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

# 通过list队列实现一个Queue类


class Queue2(list):  # 一个队列类，list的子类
    def isEmpty(self):
        return (len(self) == 0)

    def dequeue(self):  # 从队列头部移除一个项并返回一个项
        return self.pop(0)

    def denqueue(self, item):
        return self.append(item)  # 插入一个项到队列的尾部
