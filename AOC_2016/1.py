# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:25:03 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import pytest

direc = pd.read_csv("1.txt", sep=", ", header=None, engine='python').transpose().astype(str)
direc['right'] = direc[0].str[0] == 'R'
direc['n'] = direc[0].str[1:].astype(int)
direc.drop(labels=[0], axis=1, inplace=True)

def grid_walk(direc):
    [x, y, xv, yv] = [0, 0, 0, 1]
    for i in range(len(direc)):
        if direc.loc[i, 'right']:
            [xv, yv] = [yv, -xv]
        else:
            [xv, yv] = [-yv, xv]
        
        x += xv * direc.loc[i, 'n']
        y += yv * direc.loc[i, 'n']
        #print(x, y)
        
    return abs(x) + abs(y)

test1 = pd.DataFrame(data=[[True, 2], [False, 3]], columns=['right', 'n'])
test2 = pd.DataFrame(data=[[True, 2], [True, 2], [True, 2]], columns=['right', 'n'])
test3 = pd.DataFrame(data=[[True, 5], [False, 5], [True, 5], [True, 3]], columns=['right', 'n'])

assert grid_walk(test1) == 5
assert grid_walk(test2) == 2
assert grid_walk(test3) == 12
    
print(f'Answer 1 is {grid_walk(direc)}')

def grid_walk_loc(direc):
    [x, y, xv, yv] = [0, 0, 0, 1]
    all_loc = [(0,0)]
    for i in range(len(direc)):
        if direc.loc[i, 'right']:
            [xv, yv] = [yv, -xv]
        else:
            [xv, yv] = [-yv, xv]
            
        for j in range(1, 1 + direc.loc[i, 'n']):
            new_x = x + (xv * j)
            new_y = y + (yv * j)
            #print(new_x, new_y)
            if (new_x, new_y) not in all_loc:
                all_loc.append((new_x, new_y))
            else:
                return abs(new_x) + abs(new_y)
        
        x += xv * direc.loc[i, 'n']
        y += yv * direc.loc[i, 'n']
        
        
test4 = pd.DataFrame(data=[[True, 8], [True, 4], [True, 4], [True, 8]], columns=['right', 'n'])
assert grid_walk_loc(test4) == 4

print(f'Answer 2 is {grid_walk_loc(direc)}')