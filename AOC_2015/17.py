# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 11:38:10 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

test = False

if test:
    con = np.array([20, 15, 10, 5, 5])
    fillsize = 25
else:
    con = np.array([43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38])
    fillsize = 150

L = len(con)
valid_com = []
Q = []
processed = [np.zeros(L, dtype=bool)]

for i in range(L):
    init_fill = np.zeros(L, dtype=bool)
    init_fill[i] = True
    Q.append(init_fill)

while Q:
    state = Q.pop()
    processed.append(state)
    if con[state].sum() == fillsize:
        if len(valid_com) > 0:
            if not np.any(np.all(state == valid_com, axis=1)):
                valid_com.append(state)
        else:
            valid_com.append(state)
    elif con[state].sum() > fillsize:
        pass
    else:
        unfilled = np.where(state==False)[0]
        for i in unfilled:
            new_state = state.copy()
            new_state[i] = True
          
          
            if not np.any(np.all(new_state == processed, axis=1)):
                Q.append(new_state)

print(f'Answer 1 is {len(valid_com)}')


import itertools

def day16():
    bottles = list(con)
    total = 0
    for i in range(len(bottles)):
        subtotal = 0
        for combination in itertools.combinations(bottles, i):
            if sum(combination) == 150:
                subtotal += 1
        total += subtotal
        print(subtotal)
    print(total)

day16()

#print(f'Answer 2 is {}')
