# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:32:14 2024

@author: Nguyễn Đức Huy - 23730841
"""

#Bài 32(Cấu trúc Lặp)
km = float(input("Nhập quãng đường xe đi(km): "))

tien = 0
if km <=1 and km > 0:
    tien = 15000
    print("số tiền:", tien)
elif 1< km < 6:
    tien = 15000 + (km - 1) * 13500
    print("số tiền:", tien)
elif km >= 6:
    tien = 15000 + (4*13500) + (km - 5) * 11000
    print("số tiền:", tien)
if km > 120:
    tien = (15000 + (4*13500) + (km - 5) * 11000) * 0.9
    print("Số tiền của bạn là:",tien)
else:
    print("Không hợp lệ")