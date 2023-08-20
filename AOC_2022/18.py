# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 11:27:25 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# fname = '18_test.txt'
fname = '18.txt'

with open(fname, 'r') as file:
    lava = [x.split(',') for x in file.read().splitlines()]

lava = [(int(x[0]), int(x[1]), int(x[2])) for x in lava]
shift = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def lava_calc(lava):
    active_cubes = set()
    faces = 0
    for drop in lava:
        active_cubes.add(drop)
        n_adj = 0
        for dx in shift:
            if (drop[0] + dx[0], drop[1] + dx[1], drop[2] + dx[2]) in active_cubes:
                n_adj += 1
        faces += 6 - (2*n_adj)
    return [faces, active_cubes]

[faces, active_cubes] = lava_calc(lava)
    
print(f"Answer 1 is {faces}")

xmax = (max([x[0]for x in lava]), max([x[1]for x in lava]), max([x[2]for x in lava]))


free_space = set()
for i in range(-1, xmax[0]+2):
    for j in range(-1, xmax[1]+2):
        for k in range(-1, xmax[2]+2):
            if (i, j, k) not in active_cubes:
                free_space.add((i, j, k))
                
Q = [(-1, -1, -1)]

while Q:
    curr = Q.pop()
    if curr in free_space:
        free_space.discard(curr)
        for dx in shift:
            Q.append((curr[0] + dx[0], curr[1] + dx[1], curr[2] + dx[2]))

[int_faces, _] = lava_calc(free_space)

print(f"Answer 2 is {faces-int_faces}")
