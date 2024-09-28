# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:34:37 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Bài 35(Cấu trúc lặp)
n = int(input("Nhập một số nguyên dương n: "))
if n > 0:
    S = 0
    for i in range(1, n + 1):
        S += i
    print("Kết quả là: ", S)
else:
    print("Vui lòng nhập số nguyên dương")
    