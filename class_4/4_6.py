#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4_6.py
@Time    :   2020/08/27 14:10:35
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

#班级花名册

# students=[]
# Last=input('请输入学生的姓氏： ')
# First=input('请输入学生的名字: ')
# Class=input('请输入学生的班级： ')
# Average_grade=float(input('请输入学生的平均课程成绩： '))

def roster(students):
    print('Last     First       class       Average grade')
    for student in students:
        print('{:10}{:10}{:10}{:8.2f}'.format(student[0],student[1],student[2],student[3]))
                    #注意定义内容在前，调用在后
students=[]
students.append(['DeMoines','Jim','Sophomore',3.45])
students.append(['Pierre','Sophie','Sophomore',4.0])
students.append(['Columbus','Maria','Senior',2.5])
students.append(['Phoenix','River','Junior',2.45])
students.append(['Olympis','Edgar','Junior',3.99])
roster(students)

