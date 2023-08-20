# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:21:34 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# valid_traps = [np.array([False, False, True]), np.array([True, False, False]),
#                np.array([False, True, True]), np.array([True, True, False])]
valid_traps = np.array([[False, False, True], [True, False, False],
                       [False, True, True], [True, True, False]])

test1 = np.array([False, False, True, True, False])
test2 = np.array([False, True, True, False, True, False, True, True, True, True])

def trap_iter(traps):
    n = len(traps)
    
    new_traps = np.zeros(traps.shape, dtype=bool)
    
    traps = np.pad(traps, 1)
    
    for i in range(n):
        comp = traps[i:i+3]
        if np.any(np.all(comp == valid_traps, axis=1)):
            new_traps[i] = True
    return new_traps

def trap_count(traps, rows):
    tot_safe = len(traps) - traps.sum()
    
    for i in range(rows-1):
        traps = trap_iter(traps)
        if np.any(traps) == False:
            return tot_safe
        tot_safe += len(traps) - traps.sum()
        print(i, tot_safe)
    
    return tot_safe

assert trap_count(test2, 10) == 38

trap_str = '.^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^'
_, traps = np.unique(np.array(list(trap_str)), return_inverse=True)
traps = traps.astype(bool)


print(f"Answer 1 is {trap_count(traps, 40)}")

print(f"Answer 2 is {trap_count(traps, 400000)}")
