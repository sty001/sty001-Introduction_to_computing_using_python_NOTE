#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   7_2.py
@Time    :   2020/09/04 21:27:43
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#代码注解
def f(y):                                     #全局名称f(),y是f()的局部变量
    x=2                                       #x是f()的局部变量
    return g(x)                               #g是全局名称，x是f()的局部变量
def g(y):                                     #g是全局变量，y是g()的局部变量
    global x                                  #x被修改为全局变量(局部->全局)
    x=4                                       #修改全局变量x
    return x*y                                #x是全局变量，y是g()的局部变量

x=0                                           #全局变量x最初赋值
res=f(x)                                      #res、f和x均是全局变量
print('x =  {},f(0) = {}'.format(x,res))      #res、f和x均是全局变量