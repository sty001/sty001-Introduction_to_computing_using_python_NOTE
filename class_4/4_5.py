#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4_5.py
@Time    :   2020/08/27 13:42:23
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#假设变量first last street number city state zipcode 均已经被赋值，编写一个打印语句，生成一个邮件标签

first='john'
last='Doe'
street='Main Street'
number='123'
city='AnyCity'
state='AS'
zipcode='09876'
fstring='{} {}\n{} {}\n{}, {} {}'
print(fstring.format(first,last,street,number,city,state,zipcode))