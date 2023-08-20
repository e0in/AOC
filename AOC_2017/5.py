# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:44:51 2023

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# [fname] = ["5_test.txt"]
[fname] = ["5.txt"]

with open(fname, 'r') as file:
    inst = file.read().splitlines()
inst = [int(x) for x in inst]
inst2 = inst.copy()

l = len(inst)
loc = 0
n = 0

while 0 <= loc < l:
    inst[loc] += 1
    loc += inst[loc] - 1
    n += 1
    # print(loc)
    
print(f'Answer 1 is {n}')

loc = 0
n = 0

while 0 <= loc < l:
    x = inst2[loc]
    
    if x >= 3:
        inst2[loc] -= 1
    else:
        inst2[loc] += 1
    loc += x
    n += 1
    # print(loc)
    
print(f'Answer 2 is {n}')
