# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:52:10 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

[x, y, ang] = [0, 0, 0]
# ang E = 0, S = 90, W = 180, N = 270, E = 360 = 0 

angdir = {0:'E', 90:'S', 180:'W', 270:'N'}

with open('12.txt', 'r') as file:
    direc = file.read().splitlines()

for line in direc:
    # print(line)
    inst = line[0]
    val = int(line[1:])
    if inst == 'R':
        ang += val
        ang %= 360
    elif inst == 'L':
        ang -= val
        ang %= 360
    elif inst =='F':
        inst = angdir[ang]
    
    if inst == 'E':
        x += val
    elif inst == 'W':
        x -= val
    elif inst == 'N':
        y += val
    elif inst == 'S':
        y -= val
    
    # print([x, y, angdir[ang]])
    
manhat = abs(x) + abs(y)
    
print(f'Answer 1 is {manhat}')

[x, y, xw, yw] = [0, 0, 10, 1]
revdict = {'R':'L', 'L':'R'}

for line in direc:
    inst = line[0]
    val = int(line[1:])
    
    if inst == 'E':
        xw += val
    elif inst == 'W':
        xw -= val
    elif inst == 'N':
        yw += val
    elif inst == 'S':
        yw -= val
    elif inst =='F':
        x += val*xw
        y += val*yw
        
        
    if inst == 'R' or inst == 'L':
        if val == 180:
            [xw, yw] = [-xw, -yw]
        else:
            if val == 270:
                inst = revdict[inst]
            
            if inst == 'R':
                [xw, yw] = [yw, -xw]
            else:
                [xw, yw] = [-yw, xw]
    
    print(line, x, y, xw, yw)        
    
manhat = abs(x) + abs(y)
    
print(f'Answer 2 is {manhat}')