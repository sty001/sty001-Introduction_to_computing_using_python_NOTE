#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch11.py
@Time    :   2020/09/12 20:46:03
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


from urllib.parse import urljoin
from html.parser import HTMLParser
from urllib.request import urlopen


def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()


# 重载HTMLParser处理程序
# ch11.py


class LinkParser(HTMLParser):  # HTML文档解析器，输出锚点开始标记的href属性值
    def handle_startendtag(self, tag, attrs):
        if tag == 'a':  # 如果是锚点标签
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])


# ch11.py
class Collectcor(HTMLParser):  # 将超链接URL收集并存储到一个列表中
    def __init__(self, url):  # 初始化解析器、url以及列表
        HTMLParser.__init__(self)
        self.url = url
        self.link = []

    def handle_startendtag(self, tag, attrs):  # 使用绝对路径收集超链接
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'Href':  # 构造绝对路径
                    absolute == urljoin(self.url, attr[1])
                    if absolute[:4] == ' http ':
                        self.links.append(absolute)

    def getLinks(self):  # 采用绝对路径返回超链接
        return self.links
