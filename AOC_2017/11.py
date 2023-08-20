# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:37:21 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

with open("11.txt", "r") as file:
    path = file.read()

def hex_path(path):
    max_dist = 0
    coord = np.array([0, 0, 0])
    steps = path.split(',')
    # Q S R
    direc = {'n':  np.array([0, 1, -1]), 's':  np.array([0, -1, +1]),
         'ne': np.array([1, 0, -1]), 'sw': np.array([-1, 0, +1]), 'sw\n': np.array([-1, 0, +1]),
         'nw': np.array([-1, 1, 0]), 'se': np.array([1, -1, 0])}

    for step in steps:
        coord += direc[step]
        dist = hex_dist(coord)
        if dist > max_dist:
            max_dist = dist
    
    return [coord, max_dist]

def hex_dist(coord):
    return np.abs(coord).max()


assert hex_dist(hex_path("ne,ne,ne")[0]) == 3
assert hex_dist(hex_path("ne,ne,sw,sw")[0]) == 0
assert hex_dist(hex_path("ne,ne,s,s")[0]) == 2
assert hex_dist(hex_path("se,sw,se,sw,sw")[0]) == 3

ans = hex_path(path)


print(f'Answer 1 is {hex_dist(ans[0])}')


print(f'Answer 2 is {ans[1]}')
