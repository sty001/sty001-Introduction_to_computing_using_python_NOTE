#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3_5.py
@Time    :   2020/08/26 20:48:35
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#编写一个程序，提示用户输入一个单词列表，然后在屏幕上输出所有四个字母的单词，每个单词单独占一行。

wordList = eval (input ('Enter word list: '))   #注意输入列表！！！ 如果单词输入单词则会报错  eg:['joe','sue','hani','sophie']   只会输出hani这个单词
for word in wordList:
    if len(word)==4:
        print(word)    