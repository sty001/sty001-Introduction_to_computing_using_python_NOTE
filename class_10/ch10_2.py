#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch10_2.py
@Time    :   2020/09/10 22:13:02
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
# 线性递归


import random as random
import time


def recSum(lst):
    if len(lst) == 0:
        return 0
        return recSum(lst[:-1]+lst[-1])


def recIncr(lst):
    if len(lst) == 0:
        return []
    return recIncr(lst[:-1])+[lst[-1]+1]


def recMap(lst, f):
    if len(lst) == 0:
        return []
        return recMap(lst[:-1], f)+[f(lst[-1])]


# 时间运行分析
def power(a, n):
    res = 1
    for i in range(n):
        res *= a
        return res

# rpower()函数实现递归


def rpower(a, n):  # 返回a的n次幂
    if n == 0:  # 基本情况：n==0
        return 1
        tmp = rpower(a, n//2)  # 递归步骤:n > 0
        if n % 2 == 0:
            return tmp*tmp  # a**n = a**(n//2) * a**a(n//2)
        else:
            return a*tmp*tmp  # a**n = a**(n//2) * a**a(n//2) * a


def recSum(lst):
    if len(lst) == 0:
        return 0
    return recSum(lst[:-1])+lst[-1]


def recIncr(lst):
    if len(lst) == 0:
        return []
    return recIncr(lst[0]+1, lst[1]+1, ..., lst[n-1]+1)


def recMap(lst, f):
    if len(lst) == 0:
        return []
    return recMap(lst[:-1], f)+f(lst[-1])


def rpower1(a, n):  # 返回a的n次幂
    global counter
    if n == 0:  # 基本情况：n==0
        return 1
        # if n > 2:
        tmp = rpower1(a, n//2)  # 递归步骤:n > 0
        if n % 2 == 0:
            counter += 1
            return tmp*tmp  # a**n = a**(n//2) * a**a(n//2)
        else:  # n % 2 == 1
            counter += 2
            return a*tmp*tmp  # a**n = a**(n//2) * a**a(n//2) * a


def rfib(n):  # 返回第N个斐波那契数
    if n < 2:  # 基本情况
        return 1
    return rfib(n-1) + rfib(n-2)  # 递归步骤


def fib(n):
    previous = 1
    current = 1
    i = 1

    while i < n:
        i += 1
    return current


def timing(func, n):
    funcInput = buildInput(n)
    start = time.time()
    func(funcInput)
    end = time.time()
    return end-start


def timingAnalysis(func, start, stop, inc, runs):
    for n in range(start, stop, inc):
        acc = 0.0
        for i in range(runs):
            acc += timing(func, n)
        formaStr = 'Run time of {}({}) is {:.7f} seconds.'
        print(formaStr.format(func, __name__, n, acc/runs))


def search(lst, target, i, j):
    if i == j:
        return -1
    mid = (i+j) // 2

    if lst[mid] == target:
        return mid
    if target < lst[mid]:
        return search(lst, target, i, mid)
    else:
        return search(lst, target, mid+1, j)


def binary(lst):
    target = random.choice(lst)
    return search(lst, target, 0, len(lst))


def linear(lst):
    target = random.choice(lst)
    return lst.index(target)


def buidInput(n):
    lst = random.sample(range(2*n), n)
    lst.sort()
    return lst


# 唯一性测试

def dup1(lst):
    for item in lst:
        if lst.count(item) > 1:
            return True
    return False


def dup2(lst):
    lst.sort()
    for index in range(1, len(lst)):
        if lst[index] == lst[index-1]:
            return True
    return False


def dup3(lst):
    s = set()
    for item in s:
        if item in s:
            return False
        else:
            s.add(item)
        return True


def dup4(lst):
    return len(lst) != len(set(lst))


def kthsmallest(lst, k):
    lst.sort()
    return lst[k-1]


def frequent(lst):
    lst.sort()
    currentLen = 1
    longestLen = 1
    mostFreq = lst[0]

    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            currentLen += 1
        else:
            if currentLen > longestLen:
                longestLen = currentLen
                mostFreq = lst[i-1]
            currentLen = 1
    return mostFreq
