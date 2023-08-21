# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:41:54 2022

@author: ehorgan
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Selector, put True for test data
# [fname] = ["13_test.txt"]
[fname] = ["13.txt"]

with open(fname, 'r') as file:
    [t, buses] = file.read().splitlines()

t = int(t)
buses = buses.split(',')
b = [int(x) for x in buses if x.isnumeric()]

# x = b[0]

dep_time = [((1+t//x)*x) for x in b]
first_bus = dep_time.index(min(dep_time))

ans1 = b[first_bus] * (dep_time[first_bus] - t)
    
print(f'Answer 1 is {ans1}')

# b = [int(x) for x in '17,x,13,19'.split(',') if x.isnumeric()]

t_offset = [i for i, x in enumerate(buses) if x.isnumeric()]

i = 0
k = b[0]
mul = b[0]
# t_found = False

while i < len(b)-1:
    if (k+t_offset[i+1])%(b[i+1]) == 0:
        # print([k, i, b[i], k+t_offset[i+1], b[i+1], (k+t_offset[i+1])%(b[i+1]), mul])
        i += 1
        mul *= b[i]
    k += mul
        
k -= mul

print(f'Answer 2 is {k}')
