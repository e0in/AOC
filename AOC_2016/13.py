# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 23:11:01 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest


def maze_gen(n, xmax=80, ymax=80):
    maze = np.zeros([ymax, xmax], dtype=bool)
    for x in range(xmax):
        for y in range(ymax):
            val = 2*x + (x+y)*(x+y+1) + n
            if not bool(bin(val)[2:].count('1')%2):
                maze[y, x] = True
    
    return maze

def maze_solve(maze, x_targ, y_targ, x_init=1, y_init=1):
    distance = np.empty(maze.shape, dtype=int)
    distance[:] = np.iinfo(distance.dtype).max
    (ymax, xmax) = maze.shape
    
    Q = [[x_init, y_init, 0]]
    
    while Q:
        [x, y, d] = Q.pop()
        
        if d < distance[y, x]:
            distance[y, x] = d
            
            for coords in [[x,y+1],[x,y-1],[x-1,y],[x+1,y]]:
                if (0 <= coords[1] < ymax) and (0 <= coords[0] < xmax):
                    
                
                    if maze[coords[1], coords[0]]:
                        Q.append(coords + [d+1])
    
    return distance[y_targ, x_targ], (distance <= 50).sum()
    

test1 = maze_gen(10, 10, 7)
assert maze_solve(test1, 7, 4)[0] == 11

maze = maze_gen(1364)

ans = maze_solve(maze, 31, 39)

print(f"Answer 1 is {ans[0]}")

print(f'Answer 2 is {ans[1]}')