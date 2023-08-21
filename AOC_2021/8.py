# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:06:40 2021

@author: ehorgan
"""

import numpy as np
import pandas as pd

test = pd.read_csv("8_test.txt", sep=" ", header=None, engine='python')
input8 = pd.read_csv("8.txt", sep=" ", header=None, engine='python')

# # Selector, put True for test data
if False:
    df = test
else:
    df = input8

patterns = df.iloc[:,0:10]
digits = df.iloc[:,11:15]

dlen = pd.concat([digits[i].str.len() for i in range(11, 15)])

vals = dlen.value_counts()

easy_digits = vals[7] + vals[2] + vals[3] + vals[4]

print(f'Answer 1 is {easy_digits}')

total = 0
conv = {'ABCDEF': '0', 'BC': '1', 'ABDEG': '2', 'ABCDG': '3', 'BCFG': '4',
        'ACDFG': '5', 'ACDEFG': '6', 'ABC': '7', 'ABCDEFG': '8', 'ABCDFG': '9'}

possibilities = pd.DataFrame(np.ones([7,7], dtype=bool),
                             index=['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                             columns=['A', 'B', 'C', 'D', 'E', 'F', 'G'])

#%% Create map

for i in range(len(df)):
    
    pos = possibilities.copy()
    pat = patterns.iloc[i,:]
    dig = digits.iloc[i,:]
    
    # Number 1, 2 segments, B and C
    in1 = pat[pat.str.len()==2].squeeze()
    pos.loc[:, 'B':'C'] = ~pos.loc[:, 'B':'C']
    
    for seg in [in1[a] for a in [0,1]]:
        pos.loc[seg, :] = ~pos.loc[seg, :]
        
    #Count occurances of B/C, B has 8, C has 9
    segBC = list(in1)
    if pat.str.count(segBC[0]).sum() == 8:
        [segB, segC] = segBC
    else:
        [segC, segB] = segBC
    
    pos.loc[segB, 'C'] = False
    pos.loc[segC, 'B'] = False
        
    # Number 1, 3 segments, A, B and C
    in7 = pat[pat.str.len()==3].squeeze()
    segA = list(set(in7) - set(in1))[0]
    
    pos.loc[:, 'A'] = False
    pos.loc[segA, 'A'] = True
    pos.loc[segA, 'D':'G'] = False
    
    # Number 4, 4 segments, B, C, F and G
    in4 = pat[pat.str.len()==4].squeeze()
    segFG = list(set(in4) - set(in1))
    
    pos.loc[segFG, 'D':'E'] = False
    pos.loc[:, 'F':'G'] = False
    pos.loc[segFG, 'F':'G'] = True
    
    #Count occurances of F/G, G has 7 , F 6
    if pat.str.count(segFG[0]).sum() == 7:
        [segG, segF] = segFG
    else:
        [segF, segG] = segFG
    
    pos.loc[segF, 'G'] = False
    pos.loc[segG, 'F'] = False
    
    segDE = list({'a', 'b', 'c', 'd', 'e', 'f', 'g'} - set(segFG) - set(in7))
    
    #Count occurances of D/E, D has 7, E has 4
    if pat.str.count(segDE[0]).sum() == 7:
        [segD, segE] = segDE
    else:
        [segE, segD] = segDE
    
    pos.loc[segD, 'E'] = False
    pos.loc[segE, 'D'] = False
    
    segmap = {}
    
    for seg in pos.columns.tolist():
        segmap[pos.loc[pos[seg], seg].index[0]] = seg
        
    #%% Convert to num
    out_value = []
    
    for j in range(4):
        outtext = []
        intext = dig.iloc[j]
        for char in intext:
            outtext.append(segmap[char])
        outtext.sort()
        outsegs = ''.join(outtext)
        
        out_value.append(conv[outsegs])
        
    total += int(''.join(out_value))
    
print(f'Answer 2 is {total}')
