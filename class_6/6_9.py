#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6_9.py
@Time    :   2020/09/04 20:18:29
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#实现函数guess(),到一个整数n作为输入参数，实现一个简单的交互式猜数游戏
import random
def guess(n):
    secret =random.randrange(0,n)
    while True:
        guess=eval(input('Enter you guess: '))
        if guess == secret:
            print ('you got it!')
            break
        elif guess < secret:
            print('too low.')
        else:
            print('too high.')


number=int(input('请输入随机数的取值范围最大值： '))
Actual_value=guess(number)