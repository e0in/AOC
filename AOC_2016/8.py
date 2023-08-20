# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:25:03 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

with open('8.txt', 'r') as file:
    inst = file.read().splitlines()

screen = np.zeros((6, 50), dtype=bool)

for line in inst:
    if line[:4] == 'rect':
        [a, b] = [int(x) for x in line.split(' ')[1].split('x')]
        screen[:b, :a] = True
    else:
        [_, direction, loc, _, mag] = line.split(' ')
        loc = int(loc[2:])
        mag = int(mag)
        if direction == 'row':
            screen[loc, :] = np.roll(screen[loc, :], mag)
        else:
            screen[:, loc] = np.roll(screen[:, loc], mag)
        
    
print(f'Answer 1 is {screen.sum()}')

plt.imshow(screen)
# EOARGPHYAO
# print(f'Answer 2 is {}')