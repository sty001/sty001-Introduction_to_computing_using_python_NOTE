#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   11_3.py
@Time    :   2020/09/13 19:46:05
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#扩展类Collector的功能，使得他可以收集所有的文本数据的一个字符串，可以使用方法getDate()获取收集的文本数据
from html.parser import HTMLParser
def handle_date(self,data):
  #收集并且拼接文本数据
  self.text+=data
def getData(self):
  #返回所有文本数据的拼接结果
  return self.text