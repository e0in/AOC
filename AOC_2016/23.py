# -*- coding: utf-8 -*-
"""
Created on Thu May  5 23:42:35 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

regs = {'a':0, 'b':0, 'c':0, 'd':0}

with open('25.txt', 'r') as file:
    inst = file.read().splitlines()
    
inst = [line.split(' ') for line in inst]
    
def bunny_code(inst, regs):
    out = []
    i = 0
    
    while i < len(inst) and len(out) < 2:
        if i == 20:
            print(regs)
        
        
        ops = inst[i]
        
        if ops[0] == 'inc':
            regs[ops[1]] += 1
            i += 1
        elif ops[0] == 'dec':
            regs[ops[1]] -= 1
            i += 1
        elif ops[0] == 'cpy':
            if not ops[2].lstrip('-').isnumeric():
                if ops[1].lstrip('-').isnumeric():
                    regs[ops[2]] = int(ops[1])
                else:
                    regs[ops[2]] = regs[ops[1]]
            i += 1
        elif ops[0] == 'jnz':
            if ops[1].lstrip('-').isnumeric():
                x = int(ops[1])
            else:
                x = regs[ops[1]]
            if x != 0:
                #print(ops, regs)
                
                if ops[2].lstrip('-').isnumeric():
                    j = int(ops[2])
                else:
                    j = regs[ops[2]]
                i += j
            else:
                i += 1
        elif ops[0] == 'tgl':
            if ops[1].lstrip('-').isnumeric():
                x = int(ops[1])
            else:
                x = regs[ops[1]]
            j = i + x
            
            if 0 <= j < len(inst):
                if inst[j][0] == 'inc':
                    inst[j][0] = 'dec'
                elif (inst[j][0] == 'dec') or (inst[j][0] == 'tgl'):
                    inst[j][0] = 'inc'
                elif inst[j][0] == 'jnz':
                    inst[j][0] = 'cpy'
                else:
                    inst[j][0] = 'jnz'
            i += 1
        elif ops[0] == 'out':
            if ops[1].lstrip('-').isnumeric():
                x = int(ops[1])
            else:
                x = regs[ops[1]]
            out.append(x)
    return out

a = -1 # 24000
while a<1:
    a += 1
    out = bunny_code(inst[8:], {'a':0, 'b':0, 'c':0, 'd':a+2538})
    print(a, out)
    if out == [0, 1] or out == [1, 0]:
        ans = a
        print(f"Answer 1 is {a}")
        break
 
    # 2730-2538 == 192 # broken somewhere
# print(f"Answer 1 is {bunny_code(regs)}")

# regs = {'a':12, 'b':0, 'c':0, 'd':0}

# print(f'Answer 2 is {bunny_code(regs)}')

