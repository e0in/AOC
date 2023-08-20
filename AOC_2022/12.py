# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:00:14 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from copy import deepcopy

# import sys
import heapq
# import itertools
# from collections import defaultdict, Counter, deque

test = pd.read_csv("12_test.txt", sep = '', header=None, engine='python')
inputdat = pd.read_csv("12.txt", sep = '', header=None, engine='python')

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

init_loc = list(zip(*np.where(trees_arr == 'S')))[0] # (y, x)
trees_arr[trees_arr == 'S'] = 'a'
dest_loc = list(zip(*np.where(trees_arr == 'E')))[0] # (y, x)
trees_arr[trees_arr == 'E'] = 'z'

vec_ord = np.vectorize(lambda t: ord(t))
H = vec_ord(trees_arr)-97

Q = [[0, init_loc]]
D = np.full([l, w], np.inf, dtype=int)
#D[:, :] = np.nan
DX = [-1,0,1,0]
DY = [0,1,0,-1]

while Q:
    (dist, yx) = heapq.heappop(Q)
    
    
    if (D[yx] < 0) or (dist < D[yx]):
        D[yx] = dist
        
        [y, x] = yx
        
        for d in range(4):
            dx = x+DX[d]
            dy = y+DY[d]
            dyx = (dy, dx)
            if (0 <= dx < w) and (0 <= dy < l) and (H[dyx] <= H[yx]+1):
                heapq.heappush(Q, [dist+1, dyx])

print(f'Answer 1 is {D[dest_loc]}')
D[D<0] = -1
plt.imshow(D)


low_loc = list(zip(*np.where(H == 0)))
Q = [[0, x] for x in low_loc] # (y, x)
D2 = np.full([l, w], np.inf, dtype=int)

while Q:
    (dist, yx) = heapq.heappop(Q)
    
    
    if (D2[yx] < 0) or (dist < D2[yx]):
        D2[yx] = dist
        
        [y, x] = yx
        
        for d in range(4):
            dx = x+DX[d]
            dy = y+DY[d]
            dyx = (dy, dx)
            if (0 <= dx < w) and (0 <= dy < l) and (H[dyx] <= H[yx]+1):
                heapq.heappush(Q, [dist+1, dyx])

print(f'Answer 2 is {D2[dest_loc]}')

D2[D2<0] = -1
plt.imshow(D2)
