# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 21:31:31 2023

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

trgt = 265149

def loc_xy(val):
    if val == 1:
        return [0, 0, 0]

    row = 0
    
    while val > (1 + 2*row)**2:
        row += 1
        # print(row, (1+2*row)**2, val)
    
    l_side = 1 + 2*row
    # l_half = l_side//2
    
    run_len = val - (1 + 2*(row-1))**2 - 1
    
    if run_len < l_side - 1:    # print("right side")
        x = row
        y = -row + 1 + run_len
    elif run_len < 2*(l_side - 1):    
        # print("top side")
        y = row
        x = row - 1 - (run_len - l_side + 1)
    elif run_len < 3*(l_side - 1):    # 
        # print("left side")
        x = -row
        y = row - 1 - (run_len - 2*l_side + 2)
    else:     
        # print("bottom side")
        y = -row
        x = -row + 1 + (run_len - 3*l_side + 3)
    
    return [abs(x)+abs(y), row, x, y]
    

assert loc_xy(12)[0] == 3
assert loc_xy(23)[0] == 2
assert loc_xy(1024)[0] == 31

print(f'Answer 1 is {loc_xy(trgt)[0]}')

from collections import defaultdict

def def_value():
    return 0

d = defaultdict(def_value)

d[(0, 0)] = 1

[x, y, n] = [1, 0, 2]

val = 1

while val < trgt:
    val = d[x-1, y+1] + d[x, y+1] + d[x+1, y+1] + d[x-1, y] + d[x+1, y] + d[x-1, y-1] + d[x, y-1] + d[x+1, y-1]
    d[x, y] = val
    n += 1
    [_, _, x, y] = loc_xy(n)
 

print(f'Answer 2 is {val}')