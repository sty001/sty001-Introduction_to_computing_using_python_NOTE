#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8_9.py
@Time    :   2020/09/05 09:27:58
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 重新实现类queue的方法dequeue()，当尝试从一个空队列中出队时，引发一个keyboardinterrupt异常


def dequeue(self):
    if len(self) == 0:
        raise KeyboardInterrupt('dequeue from empty queue')
    return self.q.pop(0)
