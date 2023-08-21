# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:10:20 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("23.txt", sep='\n', header=None, engine='python')
df = df[0].str.split(' ', expand=True)
df.columns = ['ins', 'val', 'off']
df['val'] = df['val'].str.rstrip(',')

df.loc[df['ins'] == 'jmp', 'off'] = df.loc[df['ins'] == 'jmp', 'val']
df['off'].fillna('0', inplace=True)
df['off'] = df['off'].astype(int)


def turing(df, reg):
    i = 0

    while i in df.index.tolist():
        inst = df.loc[i, :]
        if inst.ins == 'hlf':
            reg[inst.val] = round(reg[inst.val]/2)
            i += 1
        elif inst.ins == 'tpl':
            reg[inst.val] *= 3
            i += 1
        elif inst.ins == 'inc':
            reg[inst.val] += 1
            i += 1
        elif inst.ins == 'jmp':
            i += inst.off
        elif inst.ins == 'jie':
            if not bool(reg[inst.val]%2):
                i += inst.off
            else:
                i += 1
        elif inst.ins == 'jio':
            if reg[inst.val] == 1:
                i += inst.off
            else:
                i += 1
    return reg
        

reg1 = turing(df, pd.Series({'a':0, 'b':0}))

print(f'Answer 1 is {reg1["b"]}')

reg2 = turing(df, pd.Series({'a':1, 'b':0}))

print(f'Answer 2 is {reg2["b"]}')



