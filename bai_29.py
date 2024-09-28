# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:09:23 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Bài 29 (Cấu trúc lặp)

N = int(input("Nhập số nguyên dương N:"))

while N < 0:
    N = int(input("Nhập lại N:"))
s = 0 #tong = 0
for i in range(1, N + 1):
    s += N%10
    N//= 10
print(s)