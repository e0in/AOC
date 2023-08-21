# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:33:27 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from copy import deepcopy

test = pd.read_csv("5_test.txt", header=None, engine='python', skip_blank_lines=False, skipinitialspace=False)
inputdat = pd.read_csv("5.txt", header=None, engine='python', skip_blank_lines=False, skipinitialspace=False)

# Selector, put True for test data
if False:
    df = test
else:
    df = inputdat

sep_loc = np.where(df.isnull().squeeze())[0][0]
n = int(df[0][sep_loc-1].split()[-1])

stacks = pd.Series([[] for i in range(n+1)])

inst = df[0][sep_loc+1:].str.split(' ', expand=True)
inst.drop(columns = [0, 2, 4], inplace = True)
inst = inst.astype(int)
inst.reset_index(inplace = True, drop=True)
inst.columns = ['n', 'a', 'b']

for i in range(1, n+1):
    for j in range(sep_loc-2, -1, -1):
        try:
            c = df[0][j][-3 + i*4]
        except:
            pass
        
        if c.isalpha():
            stacks[i].append(c)
            
stacks2 = stacks.apply(deepcopy)
            
def stackmove(stacks, a, b, n=1):
    val = stacks[a].pop()
    stacks[b].append(val)
    
    n -= 1
    if n == 0:
        return stacks
    else:
        return stackmove(stacks, a, b, n)
    
for i in range(len(inst)):
    stacks = stackmove(stacks, inst.loc[i, 'a'], inst.loc[i, 'b'], inst.loc[i, 'n'])

for i in range(1, n+1):
    stacks[0].append(stacks[i][-1])

print(f'Answer 1 is {"".join(stacks[0])}')

def stackmove2(stacks2, a, b, n=1):
    val = []
    
    for i in range(n):
        val.append(stacks2[a].pop())
    val.reverse() # Could remove this line and use for part one as well
        
    stacks2[b] += val
    
    return stacks2

for i in range(len(inst)):
    stacks2 = stackmove2(stacks2, inst.loc[i, 'a'], inst.loc[i, 'b'], inst.loc[i, 'n'])

for i in range(1, n+1):
    stacks2[0].append(stacks2[i][-1])


print(f'Answer 2 is {"".join(stacks2[0])}')

