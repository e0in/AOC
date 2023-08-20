# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:22:52 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

from collections import deque

# prog = list('abcde')
# dance = ['s1', 'x3/4', 'pe/b']

def spin_lock(jmp = 3, n = 2017):
    spinlock = deque([0])
    
    for i in range(1, n):
        spinlock.rotate(-jmp)
        spinlock.append(i)
        # print(len(arr), arr[np.where(arr == 0)[0][0]+1])
    
    return(spinlock)


arr = spin_lock(3, 2018)

print(f'Answer 1 is {arr[0]}')

arr2 = spin_lock(304, 50000001)

print(f'Answer 2 is {arr2[arr2.index(0) + 1]}')

