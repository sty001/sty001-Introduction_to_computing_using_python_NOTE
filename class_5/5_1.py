#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5_1.py
@Time    :   2020/08/28 23:28:42
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#计算BMI 身体质量指数

def myBMI(weight,height):
    bmi=weight / height**2    # kg  m 
    #bmi=weight*703 / height**2  # 英寸 磅
    print(bmi)
    if bmi < 18.5:
        print ('体重过轻')
    elif bmi < 25:
        print ('正常体重')
    else:
        print('体重过重')

weight=float(input('请输入您的体重kg： '))
height=float(input('请输入您的身高m： '))
BMI=myBMI(weight,height)