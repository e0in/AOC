# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:17:49 2021

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import itertools
import tqdm

test = pd.read_csv("9_test.txt", sep=" = ", header=None, engine = 'python')
input9 = pd.read_csv("9.txt", sep=" = ", header=None, engine = 'python')

# Change to True for test data, False for real
if False:
    df = test
else:
    df = input9

df[['l1', 'l2']] = df[0].str.split(' to ', expand=True)
df.drop(0, inplace=True, axis = 1)
df.rename(columns={1:"dist"}, inplace=True)

df['t1'] = list(zip(df['l1'], df['l2']))
df['t2'] = list(zip(df['l2'], df['l1']))
places = list(set(pd.concat([df['l1'], df['l2']]).tolist()))

n = len(places)
mindist = 9999999
minorder = -1

order = list(itertools.permutations(places, n))

# for i in tqdm.trange(len(order)):
#     dist = 0
#     route = order[i]
#     for j in range(n-1):
#         section = route[j:j+2]
#         sect_dist = df.loc[(df['t1'] == section) | (df['t2'] == section), 'dist'].squeeze()
#         dist += sect_dist
    
#     if dist < mindist:
#         mindist = dist
#         minorder = i

# print(f'Answer 1 is {mindist}')

maxdist = 0
maxorder = -1

for i in tqdm.trange(len(order)):
    dist = 0
    route = order[i]
    for j in range(n-1):
        section = route[j:j+2]
        sect_dist = df.loc[(df['t1'] == section) | (df['t2'] == section), 'dist'].squeeze()
        dist += sect_dist
    
    if dist > maxdist:
        maxdist = dist
        maxorder = i

print(f'Answer 2 is {maxdist}')