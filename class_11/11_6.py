#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   11_6.py
@Time    :   2020/09/13 19:49:43
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#开发函数frequency()，带一个字符串作为输入参数，计算每个单词在字符串中出现的频率，返回一个字典，把字符串中的单词映射到其频率，要求使用一个正则表达式来获取字符串中所有的单词列表
def frequency(content):
  pattern=' [a-zA-Z]+'
  words =findall(pattern,content)
  dictionary= {}
  for w in words:
    if w in dictionary:
      dictionary[w] +=1
    else:
      dictionary[w] =1
  return dictionary
  
