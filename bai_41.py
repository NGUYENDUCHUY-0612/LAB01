# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:23:20 2024

@author: ADM
"""

#Bài 41

s = 0
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("nhap lai n"))

for i in range(1, n+1):
   
    s += 1/(2*i+1)
print(round(s, 2))