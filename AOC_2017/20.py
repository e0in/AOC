# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:49:07 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest


parts = pd.read_csv("20.txt", sep=", ", header=None, names = ["p", "v", "a"], engine='python')

for col in ["p", "v", "a"]:
    parts[col] = parts[col].apply(lambda st: st[st.find("<")+1:st.find(">")])

parts['no'] = parts.index
    
arr_p = parts['p'].str.split(',', expand=True).astype(int).to_numpy()
arr_v = parts['v'].str.split(',', expand=True).astype(int).to_numpy()
arr_a = parts['a'].str.split(',', expand=True).astype(int).to_numpy()

# dist = parts['x'].abs() + parts['y'].abs() + parts['z'].abs()

# p_arr = parts[['x', 'y', 'z']].to_numpy()

dist = np.sum(np.abs(arr_p), axis=1)

closest = dist.argmin()

# count = 0
# i = 0

# while count < 1000:
#     i += 1
#     arr_v += arr_a
#     arr_p += arr_v

#     dist = np.sum(np.abs(arr_p), axis=1)

#     new_closest = dist.argmin()

#     if new_closest == closest:
#         count += 1
#     else:
#         closest = new_closest
#         count = 0
#         print(f'Iteration {i}, particle {closest}')

# print(f'Answer 1 is {closest}')

for i in range(10000):
    arr_v += arr_a
    arr_p += arr_v
    
    unq, count = np.unique(arr_p, axis=0, return_counts=True)
    
    repeated_groups = unq[count > 1]
    
    if len(repeated_groups) > 0:
        repeats = []
    
        for repeated_group in repeated_groups:
            repeated_idx = np.argwhere(np.all(arr_p == repeated_group, axis=1))
            repeats += list(repeated_idx.ravel())
            
        arr_p = np.delete(arr_p, repeats, axis=0)
        arr_v = np.delete(arr_v, repeats, axis=0)
        arr_a = np.delete(arr_a, repeats, axis=0)


print(f'Answer 2 is {len(arr_v)}')