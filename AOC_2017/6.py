# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 19:27:45 2023

@author: Eoin
"""


import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# [fname] = ["5_test.txt"]
# [fname] = ["6.txt"]

arr = np.array([0, 2, 7, 0], dtype=np.ushort)
arr = np.array([4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5], dtype=np.ushort)

l = len(arr)
states = list()
states.append(list(arr))
n = 0

found = False

while not found:
    loc = np.argmax(arr)
    val = arr[loc]
    arr[loc] = 0
    
    arr += val//l
    
    if val%l > 0:
        arr = np.roll(arr, -loc-1)
        arr[:val%l] += 1
        arr = np.roll(arr, +loc+1)
    
    n += 1
    
    if list(arr) not in states:
        states.append(list(arr))
    else:
        found = True
        states.append(list(arr))

    
print(f'Answer 1 is {n}')

loc = states.index(states[-1])

print(f'Answer 2 is {len(states) - 1 - loc}')