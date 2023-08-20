# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:27:32 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest
import itertools

def djikstra(duct, y_0, x_0):
    w = len(duct[0])
    h = len(duct)
    Q = [[y_0, x_0, 0]]
    D = 100000 * np.ones([h, w], dtype = int)
    
    while Q:
        [y, x, steps] = Q.pop()
        if 0 <= x < w and 0 <= y < h:
            if duct[y][x] != '#':
                if D[y, x] > steps:
                    D[y, x] = steps
                    Q.append([y+1, x, steps+1])
                    Q.append([y-1, x, steps+1])
                    Q.append([y, x+1, steps+1])
                    Q.append([y, x-1, steps+1])
    return D

def shortest_path(fname, max_site):

    with open(fname, 'r') as file:
        duct = file.read()#.splitlines()
    
    loc = []
    for i in range(max_site+1):
        loc.append(duct.find(str(i)))
    
    duct = duct.splitlines()
    w_n = len(duct[0])+1
    
    coords = [(x//w_n, x%w_n) for x in loc] # (y, x)
    path_lens = np.zeros([max_site+1, max_site+1], dtype=int)
    

    for i in range(max_site):
        paths = djikstra(duct, coords[i][0], coords[i][1])
        for j in range(i, max_site+1):
            path_lens[i, j] = path_lens[j, i] = paths[coords[j][0], coords[j][1]]
            
    max_steps = 1000000
    ret_max_steps = 1000000
    
    for order in list(itertools.permutations(list(range(1, max_site+1)))):
        cur_steps = 0
        b = 0
        
        for point in order:
            a = b
            b = point
            cur_steps += path_lens[a, b]
        
        ret_steps = cur_steps + path_lens[b, 0]
        
        if cur_steps < max_steps:
            max_steps = cur_steps
        
        if ret_steps < ret_max_steps:
            ret_max_steps = ret_steps

    return max_steps, ret_max_steps

assert shortest_path('24_test.txt', 4)[0] == 14

ans = shortest_path('24.txt', 7)

print(f"Answer 1 is {ans[0]}")

print(f"Answer 2 is {ans[1]}")
