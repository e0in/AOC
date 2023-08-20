# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 23:11:01 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

regs = {'a':0, 'b':0, 'c':0, 'd':0}

with open('12.txt', 'r') as file:
    inst = file.read().splitlines()
    
def bunny_code(regs):
    i = 0
    
    while i < len(inst):
        ops = inst[i].split(' ')
        
        if ops[0] == 'inc':
            regs[ops[1]] += 1
            i += 1
        elif ops[0] == 'dec':
            regs[ops[1]] -= 1
            i += 1
        elif ops[0] == 'cpy':
            if ops[1].isdigit():
                regs[ops[2]] = int(ops[1])
            else:
                regs[ops[2]] = regs[ops[1]]
            
            i += 1
        
        else:
            if ops[1].isdigit():
                x = int(ops[1])
            else:
                x = regs[ops[1]]
            
            
            if x != 0:
                i += int(ops[2])
            else:
                i += 1
    return regs['a']
        

print(f"Answer 1 is {bunny_code(regs)}")


regs['c'] = 1

print(f'Answer 2 is {bunny_code(regs)}')