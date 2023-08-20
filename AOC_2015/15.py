# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 20:51:12 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd

real = True

if real:
    fname = "15.txt"
else:
    fname = "15_test.txt"

df = pd.read_csv(fname, sep=" ", header=None, engine='python')
df = df[[0, 2, 4, 6, 8, 10]]

df.columns = ['name', 'capacity', 'durability', 'flavor', 'texture', 'calories']
df['name'] = df['name'].str.rstrip(':')
df.iloc[:, 1:5] = df.iloc[:, 1:5].apply(lambda x: x.str.rstrip(',')).astype(int)

maxscore = 0
if real: # brute force method
    for B in range(100):
        for A in range(100-B):
            for C in range(100-B-A):
                S = 100 - C - A - B
                if S >= 0:
                    quant = [S, B, C, A]
                    score = [(df['capacity'] * quant).sum(), (df['durability'] * quant).sum(),
                              (df['flavor'] * quant).sum(), (df['texture'] * quant).sum()]
                    score = np.prod([(elem if elem > 0 else 0) for elem in score])
                    if score > maxscore:
                        maxscore = score
else:
    for B in range(100):
        C = 100 - B
        quant = [B, C]
        score = [(df['capacity'] * quant).sum(), (df['durability'] * quant).sum(),
                  (df['flavor'] * quant).sum(), (df['texture'] * quant).sum()]
        score = np.prod([(elem if elem > 0 else 0) for elem in score])
        if score > maxscore:
            maxscore = score

# Attempt to constrain search such that no term goes to zero. 
# if real:
#     for B in [0, 1, 2, 3]:
#         for A in range(5*B):
#             for C in range(5*A):
#                 S = 100 - C - A - B
#                 if S >= 0:
#                     quant = [S, B, C, A]
#                     score = [(df['capacity'] * quant).sum(), (df['durability'] * quant).sum(),
#                              (df['flavor'] * quant).sum(), (df['texture'] * quant).sum()]
#                     score = np.prod([(elem if elem > 0 else 0) for elem in score])
#                     if score > maxscore:
#                         maxscore = score

            
print(f'Answer 1 is {maxscore}')

maxscore = 0
if real: # brute force method
    for B in range(100):
        for A in range(100-B):
            for C in range(100-B-A):
                S = 100 - C - A - B
                if S >= 0:
                    quant = [S, B, C, A]
                    score = [(df['capacity'] * quant).sum(), (df['durability'] * quant).sum(),
                             (df['flavor'] * quant).sum(), (df['texture'] * quant).sum()]
                    score = np.prod([(elem if elem > 0 else 0) for elem in score])
                    if (df['calories'] * quant).sum() == 500:
                        if score > maxscore:
                            maxscore = score
else:
    for B in range(100):
        C = 100 - B
        quant = [B, C]
        score = [(df['capacity'] * quant).sum(), (df['durability'] * quant).sum(),
                  (df['flavor'] * quant).sum(), (df['texture'] * quant).sum()]
        score = np.prod([(elem if elem > 0 else 0) for elem in score])
        if (df['calories'] * quant).sum() == 500:
            if score > maxscore:
                maxscore = score

            
print(f'Answer 2 is {maxscore}')