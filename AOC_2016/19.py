# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:56:08 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

n = 5
def elf(n):
    elfs = np.ones(n, dtype=int)
    
    while (elfs>0).sum() > 1:
        for i in range(n):
            if elfs[i] > 0:
                j = i+1
                while elfs[j%n] == 0:
                    j += 1
                
                elfs[i] += elfs[j%n]
                elfs[j%n] = 0
    return np.argwhere(elfs> 0)[0][0] + 1

assert elf(5) == 3

# print(f"Answer 1 is {elf(3017957)}")

def elf_2(n):
    elfs = list(range(1, n+1))
    
    i = 0
    
    while len(elfs) > 1:
        l = len(elfs)
        
        mod = (i + math.floor(l/2))%l
        
        elfs.pop(mod)
        print(len(elfs))
        #print(elfs)
        if i <= math.floor(l/2):
            i += 1
        
        
    return elfs[0]

assert elf_2(5) == 2

print(f"Answer 2 is {elf_2(3017957)}")

target = 3017957
i = 1

while i * 3 < target:
    i *= 3

print(target - i)