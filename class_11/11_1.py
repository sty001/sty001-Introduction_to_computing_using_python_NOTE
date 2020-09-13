#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   11_1.py
@Time    :   2020/09/12 22:58:37
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def news(url, topics):
    # count in resource with  URL url the frequency of each topic in list topics
    # 下载并解码资源以获取所有的小写内容
    response = urlopen(url)
    html = response.read()
    content = html.decode().lower()
    for topic in topics:
        n = content.count(topic)
        print('{} appears {} times.'.format(topics, n))


news('www.google.com',)
