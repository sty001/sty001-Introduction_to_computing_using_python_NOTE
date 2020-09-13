#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3_11.PY
@Time    :   2020/08/26 21:10:55
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#使用for循环检测列表中是否有偶数，有则返回T 没有则返回F

def allEven(numList):
    for num in numList:
        if num%2 !=0:
            return False
    return True
    
    