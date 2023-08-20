# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 22:08:58 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

from collections import defaultdict

[fname] = ["23.txt"]

with open(fname, "r") as file:
    sounds = file.read().splitlines()

reg = defaultdict(lambda : 0)

mul_count = 0

i = 0

while (0 <= i < len(sounds)):
    snd = sounds[i]
    inst = snd.split(' ')
    [a, b, c] = [inst[0], inst[1], inst[2]]
    
    if b[-1].isnumeric():
        val_b = int(b)
    else:
        val_b = reg[b]
        

    if c[-1].isnumeric():
        val_c = int(c)
    else:
        val_c = reg[c]
        
    if a == 'jnz':
        if val_b != 0:
            i += val_c
        else:
            i += 1
            
    else:
        i += 1
    
        if a == 'set':
            reg[b] = val_c
        elif a == 'sub':
            reg[b] -= val_c
        elif a == 'mul':
            reg[b] *= val_c
            mul_count += 1
    # print([i, snd, reg])
        

print(f'Answer 1 is {mul_count}')



