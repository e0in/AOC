# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:35:05 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest


factor_A = 16807
factor_B = 48271
div = 2147483647

# [a, b] = [65, 8921]
[a, b] = [634, 301] 

# matches = 0

# for i in range(40000000):
#     a = (a*factor_A)%div
#     b = (b*factor_B)%div
    
#     if a%65536 == b%65536:
#         matches += 1

# print(f'Answer 1 is {matches}')

matches = 0
a_list = []
b_list = []

for i in range(50000000):
    a = (a*factor_A)%div
    b = (b*factor_B)%div
    
    if a%4 == 0:
        a_list.append(a%65536)
        
    if b%8 == 0:
        b_list.append(b%65536)
        
a_list = a_list[:5000000]
b_list = b_list[:5000000]

a_list = np.array(a_list)
b_list = np.array(b_list)


print(f'Answer 2 is {sum(a_list == b_list)}')

