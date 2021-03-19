# -*- coding: utf-8 -*- 
# @Time    : 2021/3/19 下午2:51
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : sum.py
# @Software: PyCharm


def sum(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


print(sum(100))
