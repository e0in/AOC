# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:04:22 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

test = pd.read_csv("19_test.txt", sep='\n\n', header=None, engine='python')
inputdat = pd.read_csv("19.txt", sep='\n\n', header=None, engine='python')

# Selector, put True for test data
if False:
    df = test
else:
    df = inputdat

mol = df.iloc[-1][0] # mol = 'HOHOHO'

reps = df.iloc[:-1][0].str.split(' => ', expand=True).rename(columns={0: "in", 1: "out"})
outmols = set()


for i in range(len(mol) - 1):
    twochar = False
    if mol[i+1].islower():
        ch = mol[i:i+2]
        i += 1
        twochar = True
    else:
        ch = mol[i]

    valid_reps = reps.loc[reps['in'] == ch, 'out']
    if len(valid_reps) > 0:
        for new_char in valid_reps:
            if twochar:
                new_str = mol[:i-1] + new_char + mol[i+1:]
            else:
                new_str = mol[:i] + new_char + mol[i+1:]
            #print(i, ch, new_char)
            outmols.add(new_str)

if i == len(mol) - 2:
    i += 1
    ch = mol[i]
    valid_reps = reps.loc[reps['in'] == ch, 'out']
    if len(valid_reps) > 0:
        for new_char in valid_reps:
            new_str = mol[:i] + new_char + mol[i+1:]
            #print(i, ch, new_char, new_str)
            outmols.add(new_str)
        

print(f'Answer 1 is {len(outmols)}')

reps['outlen'] = reps['out'].str.len()
reps.sort_values(by='outlen', ascending=False, inplace=True)

repcount = 0

while len(mol) > 1:
    i = 0
    nochange = True
    
    while nochange:
        react = reps.iloc[i,:]
        
        if mol.find(react['out']) == -1:
            i += 1
        else:
            nochange = False
            ind = mol.find(react['out'])
            mol = mol[:ind] + react['in'] + mol[ind+react['outlen']:]
            repcount += 1



print(f'Answer 2 is {repcount}')