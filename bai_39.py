# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:34:42 2024

@author: Nguyễn Đức Huy - 23730841
"""

n = int(input("Nhập vào số nguyên n: "))
S = 0
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(1, n + 1):
    S += (1 / i)
    S = float(S)
print("Tổng là: ", S)