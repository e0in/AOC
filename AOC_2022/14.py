# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:02:24 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Selector, put True for test data
if False:
    fname = "14_test.txt"
else:
    fname = "14.txt"

with open(fname, 'r') as file:
    rocks = file.read().splitlines()

rocks = [x.split(' -> ') for x in rocks]
# rocks = [tuple(x.split(',')) for x in rocks]
n = len(rocks)
for i in range(n):
    rocks[i] = [tuple([int(y) for y in x.split(',')]) for x in rocks[i]]

minx = 499
maxx = 501
maxd = 5

for line in rocks:
    for coord in line:
        [x, y] = coord
        if x < minx:
            minx = x
        elif x > maxx:
            maxx = x
        if y > maxd:
            maxd = y

cave = pd.DataFrame(np.zeros([maxd+1, maxx-minx+3]), columns=range(minx-1, maxx+2), dtype=int)

for line in rocks:
    for i in range(len(line)-1):
        xr = [line[i][0], line[i+1][0]]
        xlow = min(xr)
        xhigh = max(xr)
        yr = [line[i][1], line[i+1][1]]
        ylow = min(yr)
        yhigh = max(yr)
        cave.loc[ylow:yhigh, xlow:xhigh] = 100

#plt.imshow(cave)

# valid_place = True
# n_placed = 0

# while valid_place:
#     in_motion = True
#     xs = 500
#     ys = 0
    
#     while in_motion:
#         if (xs < minx) or (xs > maxx) or (ys >= maxd):
#             valid_place = False
#             in_motion = False
#             break
#         elif cave.loc[ys+1, xs] == 0:
#             ys += 1
#         elif cave.loc[ys+1, xs-1] == 0:
#             ys += 1
#             xs -= 1
#         elif cave.loc[ys+1, xs+1] == 0:
#             ys += 1
#             xs += 1
#         else:
#             cave.loc[ys, xs] = 50
#             n_placed += 1
#             in_motion = False

# print(f'Answer 1 is {n_placed}')  

cave2 = pd.DataFrame(np.zeros([maxd+3, 1001]), columns=range(1001), dtype=int)

for line in rocks:
    for i in range(len(line)-1):
        xr = [line[i][0], line[i+1][0]]
        xlow = min(xr)
        xhigh = max(xr)
        yr = [line[i][1], line[i+1][1]]
        ylow = min(yr)
        yhigh = max(yr)
        cave2.loc[ylow:yhigh, xlow:xhigh] = 100

cave2.loc[maxd+2, 0:1000] = 100

valid_place = True
n_placed_2 = 0

while valid_place:
    in_motion = True
    xs = 500
    ys = 0
    
    while in_motion:
        if cave2.loc[ys+1, xs] == 0:
            ys += 1
        elif cave2.loc[ys+1, xs-1] == 0:
            ys += 1
            xs -= 1
        elif cave2.loc[ys+1, xs+1] == 0:
            ys += 1
            xs += 1
        else:
            cave2.loc[ys, xs] = 50
            n_placed_2 += 1
            in_motion = False
            if ys == 0:
                valid_place = False
                break
plt.imshow(cave2)
print(f'Answer 2 is {n_placed_2}')  
