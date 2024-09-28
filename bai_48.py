# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:59:56 2024

@author: Nguyễn Đức Huy - 23730841
"""
#Bài 48
bo_nghiem = []
for x in range(1, 490):
    for y in range(1, 140):
        for z in range(1, 109):
            if 2*x + 7*y + 9*z == 979:
                bo_nghiem +=[(x,y,z)]
print(f"(x={x}, y={y}, z={z})")
min_nghiệm = bo_nghiem [0]
min_tổng = sum(min_nghiệm)
for nghiệm in bo_nghiem:
    tổng = sum(nghiệm)
if tổng < min_tổng:
    min_tổng = tổng
    min_nghiệm = nghiệm
print("Nghiệm nhỏ nhất của phương trình là",min_nghiệm,", với tổng là",min_tổng)