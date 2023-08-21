# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:06:42 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

test = pd.read_csv("11_test.txt", header=None, dtype = "str")
input11 = pd.read_csv("11.txt", header=None, dtype = "str")

# Selector, put True for test data
if False:
    df = test
else:
    df = input11

df = df[0].apply(lambda x: pd.Series(list(x))).astype(int)
n = len(df) - 1
total = 0

def dumbo_step(df):
    n_flashes = 0
    can_flash = pd.DataFrame(np.ones(df.shape, dtype=bool))
    df += 1
    
    while (df[can_flash] > 9).any().any():
        flashes = list(df[df[can_flash] > 9].stack().index)
        for yx in flashes:
            can_flash.loc[yx] = False
            n_flashes += 1
            [y1, y2] = [max(0, yx[0]-1), min(n, yx[0]+1)]
            [x1, x2] = [max(0, yx[1]-1), min(n, yx[1]+1)]
            df.loc[y1:y2, x1:x2] += 1
    
    df[~can_flash] = 0
    
    return(df, n_flashes)


for i in range(100):
    [df, p] = dumbo_step(df)
    # print(df)
    # print(p)
    total += p


print(f'Answer 1 is {total}') 

f = 0
i = 100

while f < 100:
    i += 1
    [df, f] = dumbo_step(df)

print(f'Answer 2 is {i}')