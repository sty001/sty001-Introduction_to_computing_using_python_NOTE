#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   6_4.py
@Time    :   2020/09/03 22:35:28
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#带一个文本作为输入参数，输出文本中各单词的频率，假设文本中没有标点符号，单词直接用空格分隔
def wordCount(text):
    wordList=text.split()
    counters={}
    for word in wordList:
        if word in counters:
            counters[word] +=1
        else:
            counters[word]= 1
    for word in counters:
        if counters[word]==1:
            print('{:8} appears {} time.'.format(word,counters[word]))
        else:
            print('{:8} appears {} time.'.format(word,counters[word]))