# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:34:29 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

test = np.loadtxt("5_test.txt", dtype = "str")
input5 = np.loadtxt("5.txt", dtype = "str")
instr = "dvszwmarrgswjxmb"

#print(f'Answer 1 is {input2.loc[:, "wrap"].sum()}')

nicecount = 0

def naughtyornice(instr):
    vowels = instr.count('a') + instr.count('e') + instr.count('i') + \
             instr.count('o') + instr.count('u')
    
    if vowels < 3:
        return False
    
    if "ab" in instr or "cd" in instr or "pq" in instr or "xy" in instr:
        return False
    
    for i in range(len(instr)-1):
        if instr[i] == instr[i+1]:
            return True
    
    return False

# vectorised naughty or nice
vnn = np.vectorize(naughtyornice)


print(f'Answer 1 is {sum(vnn(input5))}')

# %% Part 2

def naughtyornice2(instr):
    test1 = False
    for i in range(len(instr)-3):
        substr = instr[i:i+2]
        for j in range(i+2, len(instr)-1):
            if substr == instr[j:j+2]:
                test1 = True
                
    if not test1:
        return False
    
    for i in range(len(instr)-2):
        if instr[i] == instr[i+2]:
            return True
    
    return False

# vectorised naughty or nice
vnn2 = np.vectorize(naughtyornice2)

print(f'Answer 2 is {sum(vnn2(input5))}')
