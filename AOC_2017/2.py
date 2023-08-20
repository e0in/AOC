# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:20:00 2023

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# Selector, put True for test data
# [fname] = ["1_test.txt"]
[fname] = ["2.txt"]

spr = np.loadtxt(fname, dtype = "int")

diff = spr.max(axis=1) - spr.min(axis=1)

print(f'Answer 1 is {diff.sum()}')

test = np.array([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]])

# arr = np.fliplr(np.sort(test))
arr = np.fliplr(np.sort(spr))

[h, w] = arr.shape

divis = np.zeros(h, dtype=int)

for i in range(h):
    Found = False
    nums = arr[i, :]
    
    while not Found:
        numerator = nums[-1]
        nums = nums[:-1]
        loc = np.where((nums%numerator) == 0)[0]
        if loc.size > 0:
            Found = True
            divis[i] = nums[loc[0]]//numerator


print(f'Answer 2 is {divis.sum()}')