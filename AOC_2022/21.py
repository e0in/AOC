# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 09:59:32 2022

@author: ehorgan
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sympy import sympify
from sympy import solve

# Selector, put True for test data
# [fname] = ["21_test.txt"]
[fname] = ["21.txt"]

with open(fname, 'r') as file:
    mnk = file.read().splitlines()# x.replace(': ', '=') for x in 

valdict = {}
rem_ops = []

for i, oper in enumerate(mnk):
    op = oper.split(': ')
    if op[-1].isnumeric():
        valdict[op[0]] = int(op[1])
    else:
        rem_ops.append(op)

while rem_ops:
    curr = rem_ops.pop(0)
    res = curr[0]
    [val1, op, val2] = curr[1].split()
    
    if (val1 in valdict.keys()) and (val2 in valdict.keys()):
        [v1, v2] = [valdict[val1], valdict[val2]]
        if op == '+':
            valdict[res] = v1 + v2
        elif op == '-':
            valdict[res] = v1 - v2
        elif op == '*':
            valdict[res] = v1 * v2
        else:
            valdict[res] = v1 / v2
    else:
        rem_ops.append(curr)
    
print(f'Answer 1 is {int(valdict["root"])}')

mnk2 = [x for x in mnk if x[:4] != 'humn']
#mnk2.append('humn: x')

valdict = {}
txtdict = {'humn': 'x'}
rem_ops = []

for i, oper in enumerate(mnk2):
    op = oper.split(': ')
    if op[-1].isnumeric():
        txtdict[op[0]] = op[1]
        valdict[op[0]] = int(op[1])
    elif op[0] == 'root':
        root = op
    else:
        rem_ops.append(op)
        
while rem_ops:
    curr = rem_ops.pop(0)
    res = curr[0]
    [val1, op, val2] = curr[1].split()
    
    if (val1 in txtdict.keys()) and (val2 in txtdict.keys()):
        txtdict[res] = ' '.join(['(', txtdict[val1], op, txtdict[val2], ')'])
    else:
        rem_ops.append(curr)

eq1 = txtdict[root[1].split(' ')[0]]
eq2 = txtdict[root[1].split(' ')[2]]

# for i in [0, 2]:
#     print(root[1].split(' ')[i], txtdict[root[1].split(' ')[i]])

ans2 = solve(sympify(eq1) - sympify(eq2), 'x')[0]

print(f'Answer 2 is {ans2}')

