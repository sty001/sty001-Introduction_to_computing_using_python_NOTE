'''
Author: your name
Date: 2020-09-09 22:42:23
LastEditTime: 2020-09-09 23:12:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Introduction_to_computing_using_python_NOTE\text_1.py
'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   text_1.py
@Time    :   2020/09/09 22:42:30
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

from selenium import webdriver
browser = webdriver.Chrome(
    '‪C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get('http://www.baidu.com/')
