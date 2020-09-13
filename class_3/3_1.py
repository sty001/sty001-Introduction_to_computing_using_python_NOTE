#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3_1.py
@Time    :   2020/08/26 21:09:41
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


#练习3.1
# 
# 编写一个程序，实现如下功能：要求用户输入一个华氏温度，使用如下的公式转换输出其摄氏温度：
#celsius=（5/9）*（fahrenheit-32）

# here put the import lib

fahr =eval(input('Enter the temperature in degrees Fahrenheit: '))   
cels = (fahr-32)*5/9
print ('The the temperature in degrees Cwlsius is ',cels)
