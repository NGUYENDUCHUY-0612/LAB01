# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:18:49 2024

@author: ADM
"""

import math 
n = int(input("nhập n: "))
while n<=0:
    n=int(input("nhập lại n: "))
can_2 = math.sqrt(n)
if n == int(can_2**2):
# if math.sqrt(n) == int(math.sqrt(n))
    print("số chính phương")
else:
    print("không là số chính phương")