#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4_8.py
@Time    :   2020/08/27 22:46:32
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
#编写函数stringCount(),带两个字符串作为输入参数，文件名和目标字符串，返回目标字符串在文件中出现的次数
def stringCount(filename,target):
    infile=open(filename)
    content = infile.read()
    infile.close()
    return content.count(target)
    
# ch4.py    
# def numChars(filename):                 #返回filename中的字符个数
#     infile=open(filename,'r')
#     content= infile.read()
#     infile.close()
#     return len(content)

# def numWords(filename):
#     infile=open(filename,'r')
#     content = infile.read()
#     infile.close()
#     wordList=content.split()
#     print (wordList)
#     return len(wordList)


# def numWords(filename):
#     infile=open(filename,'r')         #打开文件
#     lineList = infile.readlines()     #读取文件内容到文本行列表
#     infile.close()
#    
#     print (wordList)                  #打印列表
#     return len(wordList)