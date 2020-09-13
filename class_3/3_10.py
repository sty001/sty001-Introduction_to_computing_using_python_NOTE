#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3_10.py
@Time    :   2020/08/26 21:04:53
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#实现函数noVowel()，带一个字符串s作为输入参数，判断输入字符串中是否含有元音字母
def noVowel(s):
    for c in s:
        if c in 'aeiouAEIOU':
            print ('输入的字符串含有元音字母： '+c)                       #直接输出所含元音字母
    return True

str=input("请输入一组字符串： ")
word=noVowel(str)