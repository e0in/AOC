# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:54:27 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd


inp = pd.read_csv("16.txt", sep=" ", header=None, engine='python')
aunt = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]

inp[2] = inp[2].str.rstrip(':')
inp[4] = inp[4].str.rstrip(':')
inp[6] = inp[6].str.rstrip(':')
inp[3] = inp[3].str.rstrip(',').astype(int)
inp[5] = inp[5].str.rstrip(',').astype(int)

df = pd.DataFrame(np.empty([500, 10]), dtype=int, 
                  columns=['children', 'cats', 'samoyeds', 'pomeranians',
                           'akitas', 'vizslas', 'goldfish', 'trees', 'cars',
                           'perfumes'])

df[:] = np.nan

for i in range(len(inp)):
    sue = inp.iloc[i, :]
    df.loc[i, sue[2]] = sue[3]
    df.loc[i, sue[4]] = sue[5]
    df.loc[i, sue[6]] = sue[7]
    
viable_sue = (df.iloc[:, 0] == aunt[0]) | (df.iloc[:, 0].isna())

for i in range(1, len(aunt)):
    new_via = (df.iloc[:, i] == aunt[i]) | (df.iloc[:, i].isna())
    viable_sue = viable_sue & new_via

sue_no = inp[viable_sue][1].squeeze()[:-1]

print(f'Answer 1 is {sue_no}')


viable_sue = (df.iloc[:, 0] == aunt[0]) | (df.iloc[:, 0].isna())

for i in range(1, len(aunt)):
    if (i == 1) or (i == 7):
        new_via = (df.iloc[:, i] > aunt[i]) | (df.iloc[:, i].isna())
    elif (i == 3) or (i == 6):
        new_via = (df.iloc[:, i] < aunt[i]) | (df.iloc[:, i].isna())
    else:
        new_via = (df.iloc[:, i] == aunt[i]) | (df.iloc[:, i].isna())
        
    viable_sue = viable_sue & new_via

sue_no = inp[viable_sue][1].squeeze()[:-1]

print(f'Answer 2 is {sue_no}')
