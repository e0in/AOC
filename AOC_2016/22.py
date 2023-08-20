# -*- coding: utf-8 -*-
"""
Created on Wed May  4 23:20:52 2022

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

nodes = pd.read_csv("22.txt", header=1, engine='python', delim_whitespace=True)

nodes['x'] = nodes['Filesystem'].str.split('-').str[-2].str.lstrip('x').astype(int)
nodes['y'] = nodes['Filesystem'].str.split('-').str[-1].str.lstrip('y').astype(int)

for col in ['Size', 'Used', 'Avail']:
    nodes[col] = nodes[col].str.rstrip('T').astype(int)
nodes['Use%'] = nodes['Use%'].str.rstrip('%').astype(int)

nodes.drop('Filesystem', axis=1, inplace=True)

# size[y, x]  -  30y 0-29   -   32x 0-31
size = nodes.pivot(index='y', columns='x', values='Size').to_numpy()
used = nodes.pivot(index='y', columns='x', values='Used').to_numpy()
avail = nodes.pivot(index='y', columns='x', values='Avail').to_numpy()

valid = 0

for i in range(len(nodes)-1):
    A = nodes.loc[i, :]
    for j in range(i, len(nodes)):
        B = nodes.loc[j, :]
        valid += int(A.Used > 0 and B.Avail >= A.Used)
        valid += int(B.Used > 0 and A.Avail >= B.Used)

print(f"Answer 1 is {valid}")

# print(f"Answer 2 is {valid_count(ip)[1]}")
