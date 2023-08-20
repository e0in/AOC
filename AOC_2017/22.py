# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 22:44:19 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

from collections import defaultdict
grid = defaultdict(int)

# [fname] = ["22_test.txt"]
[fname] = ["22.txt"]

with open(fname, "r") as file:
    nodes = file.read().splitlines()
    
l = len(nodes)
w = len(nodes[0])

pos = w//2 + l//2*1j
dx = 0 - 1j
infect = []
i = 0

for y in range(l):
    for x in range(w):
        if nodes[y][x] == '#':
            infect.append(x+y*1j)
            grid[x+y*1j] = 2
            
infect2 = infect.copy()

bursts = 10000

for k in range(bursts):
    if pos in infect:
        dx *= 0+1j
        infect.remove(pos)
    else:
        dx *= 0-1j
        infect.append(pos)
        i += 1
    
    pos += dx
    
print(f'Answer 1 is {i}')

pos = w//2 + l//2*1j
dx = 0 - 1j
i2 = 0


# CLEAN = 0
# WEAKENED = 1
# INFECTED = 2
# FLAGGED = 3
# MODULUS = 4
# ADD_AMOUNT = 2 - part_b

for k in range(10000000):
    if grid[pos] == 1:
        grid[pos] = 2
        i2 += 1
    elif grid[pos] == 2:
        dx *= 0+1j
        grid[pos] = 3
    elif grid[pos] == 3:
        dx *= -1
        grid[pos] = 0
    else:
        dx *= 0-1j
        grid[pos] = 1
    
    pos += dx

print(f'Answer 2 is {i2}')
