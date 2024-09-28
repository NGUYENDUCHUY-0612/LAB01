# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:20:12 2024

@author: ADM
"""

#Bài 45

s = 0
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("nhap lai n"))

for i in range(1, n+1):
   
    s += i/(i+1)
print(round(s, 2))