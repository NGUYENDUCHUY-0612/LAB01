# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:14:43 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Bài 28(Cấu trúc lặp)
N = int(input("Nhập số nguyên dương N:"))
while N < 0:
    N = int(input("Nhập lại số nguyên dương N:"))
for i in range(1, N + 1):
    if N%i == 0:
        print(i)