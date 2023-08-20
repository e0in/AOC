# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:11:33 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# prog = list('abcde')
# dance = ['s1', 'x3/4', 'pe/b']

prog = list('abcdefghijklmnop')
with open('16.txt', 'r') as file:
    dance = file.read().split(',')
    
perm = ["".join(prog)]


for inst in dance:
    if inst[0] == 's':
        x = int(inst[1:])
        prog = prog[-x:] + prog[:-x]
    elif inst[0] == 'x':
        vals = inst[1:].split('/')
        [a, b] = [int(x) for x in vals]
        prog[a], prog[b] = prog[b], prog[a]
    elif inst[0] == 'p':
        vals = inst[1:].split('/')
        a = prog.index(vals[0])
        b = prog.index(vals[1])
        prog[a], prog[b] = prog[b], prog[a]
    # print(prog)

print(f'Answer 1 is {"".join(prog)}')

# shift = [ord(x)-97 for x in prog]

# new_prog = [prog[x] for x in shift]

while "".join(prog) not in perm:
    perm.append("".join(prog))
    for inst in dance:
        if inst[0] == 's':
            x = int(inst[1:])
            prog = prog[-x:] + prog[:-x]
        elif inst[0] == 'x':
            vals = inst[1:].split('/')
            [a, b] = [int(x) for x in vals]
            prog[a], prog[b] = prog[b], prog[a]
        elif inst[0] == 'p':
            vals = inst[1:].split('/')
            a = prog.index(vals[0])
            b = prog.index(vals[1])
            prog[a], prog[b] = prog[b], prog[a]

order = 1000000000%len(perm)

print(f'Answer 2 is {"".join(perm[order])}')

