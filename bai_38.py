# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:33:50 2024

@author: Nguyễn Đức Huy - 23730841
"""

n = int(input("Nhập vào số n: "))
S = 1 
while n<0 or n%2==0:
    n = int(input("Nhập lại n: "))
for i in range(1, n+1):
    S *= i
print("Tích là: ", S)