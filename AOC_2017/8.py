# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:18:37 2023

@author: Eoin
"""


import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

[fname] = ["8_test.txt"]
[fname] = ["8.txt"]

from collections import defaultdict

def def_value():
    return 0

reg = defaultdict(def_value)

max_val = 0

with open(fname, 'r') as file:
    inst = file.read().splitlines()

inst = [x.split(' if ') for x in inst]

for ins in inst:
    [cmd, test] = ins
    
    [test_reg, ineq, val] = test.split()
    test_reg = str(reg[test_reg])
    # val = int(val)
    
    if eval(test_reg + ineq + val):
        [trgt_reg, sign, amt] = cmd.split()
        if sign == 'inc':
            reg[trgt_reg] += int(amt)
        else:
            reg[trgt_reg] -= int(amt)
        
        if reg[trgt_reg] > max_val:
            max_val = reg[trgt_reg]
        

print(f'Answer 1 is {max(list(reg.values()))}')
 

print(f'Answer 2 is {max_val}')