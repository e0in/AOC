# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:18:47 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from scipy.ndimage import label

test = pd.read_csv("9_test.txt", header=None, dtype = "str")
input9 = pd.read_csv("9.txt", header=None, dtype = "str")

# Selector, put True for test data
if False:
    df = test
else:
    df = input9

df = df[0].apply(lambda x: pd.Series(list(x))).astype(int)
[n, w] = df.shape

risk_level = 0
min_pos = np.zeros([n, w], dtype=int)

# add padding for peakfinding
df.insert(0, -1, 9)
df[w] = 9

df.loc[n,:] = 9
df.loc[-1,:] = 9
df.sort_index(inplace=True)
df = df.astype(int)

for i in range(w):#iterate over columns
    p, _ = find_peaks(10-df[i])
    min_pos[p-1, i] = 1

for i in range(n):#iterate over rows
    p, _ = find_peaks(10-df.loc[i,:])
    min_pos[i, p-1] += 1

#df = df.loc[0:n-1, 0:w-1]

mask = pd.DataFrame(min_pos == 2)

print(f'Answer 1 is {(df.loc[0:n-1, 0:w-1][mask]+1).sum().sum()}') # 637 too high


labels, nbins = label(df != 9)
labels = labels.reshape(-1)

print(f'Answer 2 is {np.partition(np.bincount(labels, labels != 0), nbins - 3)[-3:].prod().astype(int)}')