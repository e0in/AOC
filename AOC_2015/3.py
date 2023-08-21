# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:34:29 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd


test = list("^v^v^v^v^v")
#input3 = np.loadtxt("3.txt", dtype="str", delimiter="")

with open("3.txt", "r") as tf:
    input3 = list(tf.read())

del(tf)

x = 0
y = 0
all_loc = [f'{x}_{y}']

for i in range(len(input3)):
    if input3[i] == '^':
        y += 1
    elif input3[i] == 'v':
        y -= 1
    elif input3[i] == '>':
        x += 1
    else:
        x -= 1

    all_loc.append(f'{x}_{y}')

print(f'Answer 1 is {len(set(all_loc))}')

# %% Part 2

slist = input3[::2]
rlist = input3[1::2]

#santa
x = 0
y = 0
all_loc = [f'{x}_{y}']

for i in range(len(slist)):
    if slist[i] == '^':
        y += 1
    elif slist[i] == 'v':
        y -= 1
    elif slist[i] == '>':
        x += 1
    else:
        x -= 1

    all_loc.append(f'{x}_{y}')

#robo-santa
x = 0
y = 0

for i in range(len(rlist)):
    if rlist[i] == '^':
        y += 1
    elif rlist[i] == 'v':
        y -= 1
    elif rlist[i] == '>':
        x += 1
    else:
        x -= 1

    all_loc.append(f'{x}_{y}')

print(f'Answer 2 is {len(set(all_loc))}')