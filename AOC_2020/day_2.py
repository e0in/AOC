# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:27:43 2020

@author: Eoin
"""

import math
import numpy as np
import pandas as pd

#data = np.loadtxt('C:\Python\AOC_2020\input2.txt', dtype="str")

df = pd.read_csv('C:\Python\AOC_2020\input2.txt', sep=' ', header=None,
                 names=['num', 'char', 'pass'])

df['char'] = df['char'].str.rstrip(':')
df[['lb', 'ub']] = df['num'].str.split('-', 1, expand=True)
df[['lb', 'ub']] = df[['lb', 'ub']].apply(pd.to_numeric)
df['pass'] = df['pass'].astype("string")
df['char'] = df['char'].astype("string")

df = df[['lb', 'ub', 'char', 'pass']]

df['count'] = pd.Series(np.zeros(len(df), dtype='int'))

for i in range(len(df)):
    pass_str = df.iloc[i, 3]
    df.iloc[i, 4] = pass_str.count(df.iloc[i, 2])
    
df['passing'] = (df['count'] >= df['lb']) & (df['count'] <= df['ub'])

ans1 = df['passing'].sum()


df['n1p'] = pd.Series(np.zeros(len(df), dtype='bool'))
df['n2p'] = pd.Series(np.zeros(len(df), dtype='bool'))

for i in range(len(df)):
    pass_str = df.iloc[i, 3]
    pass_char = df.iloc[i, 2]
    n1 = df.iloc[i, 0] - 1
    n2 = df.iloc[i, 1] - 1
    df.iloc[i, 6] = pass_str[n1] == pass_char
    df.iloc[i, 7] = pass_str[n2] == pass_char

df['passing2'] = df['n1p'] ^ df['n2p']
ans2 = df['passing2'].sum()
