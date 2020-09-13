#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   11_2.py
@Time    :   2020/09/13 19:30:33
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#开发类MyHTMLParser，作为HTMLParser的子类，当传递一个HTML文件给它时，按照文档中出现的顺序打印开始标签和结束标签的名称，并且缩进与文档树结构中的元素深度成比例 忽略不需要的结束标记的HTML元素 eg：p和br

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):

  #基于深度缩进打印标记的HTML文档解析器
    def __init__(self):
      HTMLParser.__init__(self)
      self.indent=0
    def handle_startendtag(self, tag, attrs):
      #采用缩进正比于文档中标记元素深度的方式打印开始标记
      if tag not in {'br','p'}:
        print('{}{} start'.format(self.indent*' ',tag))
        self.indent+=4
    def handle_endtag(self, tag):
      #采用缩进正比于文档中标记元素深度的方式打印结束标记
      if tag not in {'br','p'}:
        self.indent-=4
        print('{}{} end'.format(self.indent*' ',tag))
    
