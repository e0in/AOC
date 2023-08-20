# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 09:57:07 2021

@author: Eoin
"""

import math
import numpy as np
import pandas as pd


if False:
    fname = "25_test.txt"
else:
    fname = "25.txt"
    
df = pd.read_csv(fname, sep=" ", header=None, engine='python')
df = df[0].apply(lambda x: pd.Series(list(x)))
[l, w] = df.shape

df = np.array(df, dtype=str)

def advance(df, n=1):
    [l, w] = df.shape

    east_facing = df == '>'
    down_facing = df == 'v'
    
    pad = np.pad(df, 1, mode='wrap')
    east_off = pad[1:-1, 2:] == '.'
    
    pad[1:-1, 1:-1][east_off & east_facing] = '.'
    pad[1:-1, -1][east_facing[:, 0] & east_off[:, 0]] = '.'
    pad[1:-1, 2:][east_off & east_facing] = '>'
    
    
    df = pad[1:-1, 2:]
    df = df[:, [w-1] + list(range(w-1))]
    
    
    pad = np.pad(df, 1, mode='wrap')
    down_off = pad[2:, 1:-1] == '.'
    
    pad[1:-1, 1:-1][down_off & down_facing] = '.'
    pad[-1, 1:-1][down_facing[0, :] & down_off[0, :]] = '.'
    pad[2:, 1:-1][down_off & down_facing] = 'v'
    
    df = pad[2:, 1:-1]
    df = df[[l-1] + list(range(l-1)), :]
    
    n -= 1
    
    if n == 0:
        return df
    else:
        return advance(df, n)

n_iter = 0
found = False


while not found:
    df_new = advance(df)
    n_iter += 1
    if (df_new == df).all():
        found = True
    else:
        df = df_new


print(f'Answer 1 is {n_iter}')