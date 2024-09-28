# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:04:03 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Bài 45
ts = 1
ms = 0
s = 0
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("nhap lai n"))
x = float(input("nhap x: "))
#x^n = x**n = ts = 1
#1+2+3+...n = ms = 0
for i in range(1, n+1):
    ts = x**i
    ms = ms + i 
    s += ts/ms
print(round(s, 2))