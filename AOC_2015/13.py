# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 22:32:08 2022

@author: Eoin
"""


import math
import numpy as np
import pandas as pd
import itertools

if True:
    fname = "13.txt"
else:
    fname = "13_test.txt"

df = pd.read_csv(fname, sep=" happiness units by sitting next to ", header=None, engine='python', names = ['a', 'p2'])

df['p2'] = df['p2'].str.rstrip('.')
df[['p1', 'would', 'sign', 'value']] = df['a'].str.split(expand=True)
df['val'] = df['value'].astype(int) * (((df['sign']=='lose').astype(int)*-2)+1)
df = df[['p1', 'p2', 'val']]

for i in range(len(df)):
    seat = df.loc[i, :]
    if sorted(seat[1::-1].tolist()) == seat[1::-1].tolist():
        temp = df.loc[i, 'p1']
        df.loc[i, 'p1'] = df.loc[i, 'p2']
        df.loc[i, 'p2'] = temp

df2 = df.groupby(['p1', 'p2']).agg('sum').reset_index()

guests = list(set(df['p1'].tolist() + df['p2'].tolist()))
l = len(guests)

max_hap = 0

# for guestlist in list(itertools.permutations(guests)):
#     hap = 0
#     for i in range(l-1):
#         pair = sorted(guestlist[i:i+2])
#         val = df2.loc[(df2['p1'] == pair[0]) & (df2['p2'] == pair[1]), 'val']
#         hap += val.iloc[0]
        
    
#     pair = sorted((guestlist[0], guestlist[-1]))
#     val = df2.loc[(df2['p1'] == pair[0]) & (df2['p2'] == pair[1]), 'val']
#     hap += val.iloc[0]
    
#     if hap > max_hap:
#         max_hap = hap


print(f'Answer 1 is {max_hap}')

max_hap_2 = 0

d = {'p1': guests, 'p2': l*['ZZ_Me'],  'val': l*[0]}
df3 = pd.DataFrame(data=d)
df = df.append(df3).reset_index(drop=True)
df4 = df.groupby(['p1', 'p2']).agg('sum').reset_index()

guests.append('ZZ_Me')
l += 1

for guestlist in list(itertools.permutations(guests)):
    hap = 0
    for i in range(l-1):
        pair = sorted(guestlist[i:i+2])
        val = df4.loc[(df4['p1'] == pair[0]) & (df4['p2'] == pair[1]), 'val']
        hap += val.iloc[0]
        
    
    pair = sorted((guestlist[0], guestlist[-1]))
    val = df4.loc[(df4['p1'] == pair[0]) & (df4['p2'] == pair[1]), 'val']
    hap += val.iloc[0]
    
    if hap > max_hap_2:
        max_hap_2 = hap


print(f'Answer 2 is {max_hap_2}')
