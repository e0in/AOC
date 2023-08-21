# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:28:04 2022

@author: ehorgan
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from copy import deepcopy

test = pd.read_csv("8_test.txt", sep = '', header=None, engine='python')
inputdat = pd.read_csv("8.txt", sep = '', header=None, engine='python')

# Selector, put True for test data
if False:
    trees = test
else:
    trees = inputdat

[l, w] = trees.shape
w -= 2
trees.drop(columns=[0,w+1], inplace=True)
trees.columns = list(range(w))
trees_arr = np.array(trees)
vis = np.zeros([l-2, w-2], dtype=bool)
vis = np.pad(vis, 1, constant_values=True)

for i in range(1, w-1):
    for j in range(1, l-1):
        u = trees_arr[0:j, i].max()
        d = trees_arr[j+1:l, i].max()
        le = trees_arr[j, 0:i].max()
        r = trees_arr[j, i+1:w].max()
        
        if trees_arr[j, i] > min(u, d, le, r):
            vis[j, i] = True
        
print(f'Answer 1 is {vis.sum()}')

view = np.zeros([l, w], dtype=int)

for i in range(1, w-1):
    for j in range(1, l-1):
        h = trees_arr[j, i]
        u = np.flip(trees_arr[0:j, i])
        d = trees_arr[j+1:l, i]
        le = np.flip(trees_arr[j, 0:i])
        r = trees_arr[j, i+1:w]
        
        scenic = []
        
        for arr in [u, d, le, r]:
            if (arr >= h).any():
                scenic.append(np.append(np.where(arr >= h), 0)[0]+1)
            else:
                scenic.append(np.where(np.append((arr >= h), True))[0][0])
        
        # scenic = [np.append(np.where(u >= h), 0)[0]+1,
        #           np.append(np.where(d >= h), 0)[0]+1,
        #           np.append(np.where(le >= h), 0)[0]+1,
        #           np.append(np.where(r >= h), 0)[0]+1]
        view[j, i] = np.prod(scenic)
        
print(f'Answer 2 is {view.max()}')
