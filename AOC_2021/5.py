# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 11:40:01 2021

@author: Eoin
"""

import math
import numpy as np
import pandas as pd

test = pd.read_csv("5_test.txt", sep=" -> ", header=None, engine = 'python')
input5 = pd.read_csv("5.txt", sep=" -> ", header=None, engine = 'python')

# Change to True for test data, False for real
if False:
    df = test
else:
    df = input5

df[['x1', 'y1']] = df[0].str.split(',', expand=True).astype(int)
df[['x2', 'y2']] = df[1].str.split(',', expand=True).astype(int)
df.drop([0, 1], inplace=True, axis = 1)
extent = int(df.max().max())+1
seafloor = np.zeros([extent, extent], dtype=int)

n = len(df)

for i in range(n):
    [x1, x2, y1, y2] = [df.iloc[i, 0], df.iloc[i, 2],
                        df.iloc[i, 1], df.iloc[i, 3]]
    if x1 == x2:
        seafloor[min(y1, y2):max(y1, y2)+1, x1] += 1 
    elif y1 == y2:
        seafloor[y1, min(x1, x2):max(x1, x2)+1] += 1


print(f'Answer 1 is {(seafloor > 1).sum()}')


seafloor = np.zeros([extent, extent], dtype=int)
for i in range(n):
    [x1, x2, y1, y2] = [df.iloc[i, 0], df.iloc[i, 2],
                        df.iloc[i, 1], df.iloc[i, 3]]

    if x1 == x2:
        seafloor[min(y1, y2):max(y1, y2)+1, x1] += 1 
    elif y1 == y2:
        seafloor[y1, min(x1, x2):max(x1, x2)+1] += 1
    else:
        l = abs(x2-x1)+1
        area = seafloor[min(y1, y2):max(y1, y2)+1,
                        min(x1, x2):max(x1, x2)+1]
        for j in range(l):
            if x2 > x1:
                if y2 > y1:
                    area[j,j] += 1
                else:
                    area[l-j-1,j] += 1
            else:
                if y2 > y1:
                    area[j,l-j-1] += 1
                else:
                    area[l-j-1,l-j-1] += 1
                    
    #print(seafloor)


print(f'Answer 2 is {(seafloor > 1).sum()}')
