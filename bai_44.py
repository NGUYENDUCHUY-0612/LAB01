# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:16:37 2024

@author: ADM
"""

#Bài 44

s = 0
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("nhap lai n"))

for i in range(1, n+1):
   
    s += (2*i +1)/(2*i+2)
print(round(s, 2))