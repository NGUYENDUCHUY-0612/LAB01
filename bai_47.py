# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:25:25 2024

@author: ADM
"""

#Bài 47
bo_nghiem = []
for x in range(1, 490):
    for y in range(1, 140):
        for z in range(1, 109):
            if 2*x + 7*y + 9*z == 979:
                bo_nghiem +=[(x,y,z)]
print(f"(x={x}, y={y}, z={z})")
max_nghiệm = bo_nghiem [0]
max_tổng = sum(max_nghiệm)
for nghiệm in bo_nghiem:
    tổng = sum(nghiệm)
if tổng > max_tổng:
    max_tổng = tổng
    max_nghiệm = nghiệm
print("Nghiệm lớn nhất của phương trình là",max_nghiệm,", với tổng là",max_tổng)