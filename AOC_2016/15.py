# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:36:37 2022

@author: Eoin
"""


import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

test1 = np.array([[5, 4], [2, 1]], dtype=int)

discs = np.array([[13, 10], [17, 15], [19, 17], [7, 1], [5, 0], [3, 1]], dtype=int)

def ball_drop(discs):
    npos = discs[:, 0]
    loc = discs[:, 1]
    n = len(loc)
    
    dt = np.arange(1, n+1)
    
    t = npos[0] - (loc[0] + 1)
    
    while not all((loc+dt+t)%npos == 0):
        t += npos[0]
    
    
    return t

assert ball_drop(test1) == 5


print(f"Answer 1 is {ball_drop(discs)}")

discs2 = np.array([[13, 10], [17, 15], [19, 17], [7, 1], [5, 0], [3, 1], [11, 0]], dtype=int)


print(f"Answer 2 is {ball_drop(discs2)}")
