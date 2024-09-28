# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:34:51 2024

@author: ADM
"""

thang = int(input("Nhập tháng 1-12: "))
nam = int(input("Nhập năm: "))
if 1 <= thang <= 12:
    #print("tháng không hợp lệ)
    if thang in {1, 3, 5, 7, 8, 10, 11}:
        ngay = 31
        #print("tháng có 31 ngày")
    elif thang == 2:
        if (nam%4 ==0 and nam%100 !=0) or nam%400 == 0:
            ngay = 29
            print("năm nhuận")
        else:
            ngay = 28
            print("Không phải năm nhuận")
    else:
        ngay = 30
        #print("tháng có 30 ngày")

print(f'tháng {thang} / năm {nam} có {ngay} ngày')
