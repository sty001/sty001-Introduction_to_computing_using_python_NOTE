#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch7.py
@Time    :   2020/09/04 21:47:08
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#多重异常处理
def readAge(filename):
    try:
        infile= open(filename)
        strAge=infile.readline()
        age=int(strAge)
        print('age is ',age)
    except IOError:
        print('Input/Output error.')
    except ValueError:
        print('Value cannot be cconverted to integer.')
    except:
        print('Other error.')

