# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 13:35:25 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
from collections import Counter

test = pd.read_csv("14_test.txt", header=None, dtype = "str", engine='python')
input14 = pd.read_csv("14.txt", header=None, dtype = "str", engine='python')

if False:
    df = test
else:
    df = input14

poly = df[0][0]

pairs = df.loc[1:, 0].str.split(" -> ", expand = True).reset_index(drop=True)

# def pairs_insertion(poly, pairs):
#     outpoly = []
#     for i in range(len(poly)-1):
#         p = poly[i:i+2]
#         outpoly.append(p[0])
#         outpoly.append(pairs.loc[p == pairs[0], 1].squeeze())
#     outpoly.append(poly[-1])

#     return("".join(outpoly))

# poly1 = poly

# for i in range(10):
#     poly1 = pairs_insertion(poly1, pairs)

# freq = {i : poly1.count(i) for i in set(poly1)}
# freq = pd.DataFrame(freq, index = [0])

# print(f'Answer 1 is {freq.max().max() - freq.min().min()}') 

paircount = Counter(map(str.__add__, poly, poly[1:]))
charcount = Counter(poly)

pairsdict = dict(zip(pairs[0], pairs[1]))

for i in range(40):
    current = paircount.copy()
    for pair in list(current.keys()):
        n = current[pair]
        c = pairsdict[pair]
        
        paircount[pair] -= n
        paircount[pair[0]+c] += n
        paircount[c+pair[1]] += n
        charcount[c] += n

print(charcount.most_common())

print(f'Answer 2 is {max(charcount.values()) - min(charcount.values())}') 