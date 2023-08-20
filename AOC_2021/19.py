# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 10:49:43 2021

@author: Eoin
"""

import math
import numpy as np
import pandas as pd

test1 = pd.read_csv("19_test.txt", sep=" scanner ", header=None, engine='python')
inputdat = pd.read_csv("19.txt", sep=" scanner ", header=None, engine='python')

if True:
    df = test1
else:
    df = inputdat
    
    
sep_index = list(df[df[1].notna()].index)
sep_index.append(len(df))

df[['x', 'y', 'z']] = df[0].str.split(',', expand=True)

zero_beacons = df.iloc[sep_index[0]+1:sep_index[1], 2:5].copy().astype(int)
# zero_beacons.sort_values(['x', 'y', 'z'], inplace=True)
zero_beacons.reset_index(drop=True, inplace=True)
#coords = list(zero_beacons.value_counts().index)

#zero_beacons_off = zero_beacons.copy()

dists = pd.DataFrame(np.zeros((600, 3)), columns = ['A', 'B', 'dist'], dtype=int)
k = 0
for i in range(len(zero_beacons)-1):
    for j in range(i+1, len(zero_beacons)):
        dist = ((zero_beacons.iloc[i, :] - zero_beacons.iloc[j, :])**2).sum()
        dists.iloc[k, :] = [i, j, dist]
        k += 1
dists.drop(dists.index[k:600], inplace=True)

rot_beacons = []

# for i in range(1, len(sep_index)-1):
#     print([sep_index[i]+1, sep_index[i+1]])
# # [27, 52]
# # [53, 79]
# # [80, 105]
# # [106, 132]

# not all beacons overlapping with zero beacon

for i in range(1, len(sep_index)-1):
    comp_beacon = df.iloc[sep_index[i]+1:sep_index[i+1], 2:5].copy().astype(int)

#comp_beacon = df.iloc[sep_index[1]+1:sep_index[1+1], 2:5].copy().astype(int)
    comp_beacon.reset_index(drop=True, inplace=True)
    
    comp_dists = pd.DataFrame(np.zeros((600, 3)), columns = ['comp_A', 'comp_B', 'dist'], dtype=int)
    k = 0
    for p in range(len(comp_beacon)-1):
        for j in range(p+1, len(comp_beacon)):
            dist = ((comp_beacon.iloc[p, :] - comp_beacon.iloc[j, :])**2).sum()
            comp_dists.iloc[k, :] = [p, j, dist]
            k += 1
    comp_dists.drop(comp_dists.index[k:600], inplace=True)
    
    matched = dists.merge(comp_dists, on='dist', how='inner')
    
    orig_beacons = list(set(matched['A'].tolist() + matched['B'].tolist()))
    zb_matches = zero_beacons.loc[orig_beacons, :]
    comp_beacons = list(set(matched['comp_A'].tolist() + matched['comp_B'].tolist()))
    comp_matches = zb_matches.copy()
    
    
    for beacon in orig_beacons:
        crit = (matched['A'] == beacon) | (matched['B'] == beacon)
        mapped_beacon = matched.loc[crit, 'comp_A':'comp_B'].stack().reset_index(drop=True).mode()[0]
        comp_matches.loc[beacon, :] = comp_beacon.iloc[mapped_beacon, :]
        
    x_found = False
    y_found = False
    xo = 0
    yo = 0
    zo = 0
    
    xdiff = zb_matches['x'] - comp_matches['x']
    if (xdiff - xdiff.iloc[0]).sum() == 0:
        x_found = True
        xo = xdiff.iloc[0]
        comp_matches['x'] = comp_matches['x']+xo
        comp_beacon['x'] = comp_beacon['x']+xo
    else:
        xdiff = zb_matches['x'] + comp_matches['x']
        if (xdiff - xdiff.iloc[0]).sum() == 0:
            x_found = True
            xo = - xdiff.iloc[0]
            comp_matches['x'] = -comp_matches['x']-xo
            comp_beacon['x'] = -comp_beacon['x']-xo
    
    while (not x_found):
        comp_matches[['x', 'y', 'z']] = comp_matches[['y', 'z', 'x']]
        xdiff = zb_matches['x'] - comp_matches['x']
        if (xdiff - xdiff.iloc[0]).sum() == 0:
            x_found = True
            xo = xdiff.iloc[0]
            comp_matches['x'] = comp_matches['x']+xo
            comp_beacon['x'] = comp_beacon['x']+xo
        else:
            xdiff = zb_matches['x'] + comp_matches['x']
            if (xdiff - xdiff.iloc[0]).sum() == 0:
                x_found = True
                xo = - xdiff.iloc[0]
                comp_matches['x'] = -comp_matches['x']-xo
                comp_beacon['x'] = -comp_beacon['x']-xo
    
    ydiff = zb_matches['y'] - comp_matches['y']
    if (ydiff - ydiff.iloc[0]).sum() == 0:
        y_found = True
        yo = ydiff.iloc[0]
        comp_matches['y'] = comp_matches['y']+yo
        comp_beacon['y'] = comp_beacon['y']+yo
    else:
        ydiff = zb_matches['y'] + comp_matches['y']
        if (ydiff - ydiff.iloc[0]).sum() == 0:
            y_found = True
            yo = - ydiff.iloc[0]
            comp_matches['y'] = -comp_matches['y']-yo
            comp_beacon['y'] = -comp_beacon['y']-yo
    
    if (not y_found):
        temp = comp_matches['y'].copy()
        comp_matches['y'] = -comp_matches['z']
        comp_matches['z'] = temp
        ydiff = zb_matches['y'] - comp_matches['y']
        if (ydiff - ydiff.iloc[0]).sum() == 0:
            y_found = True
            yo = ydiff.iloc[0]
            comp_matches['y'] = comp_matches['y']+yo
            comp_beacon['y'] = comp_beacon['y']+yo
        else:
            ydiff = zb_matches['y'] + comp_matches['y']
            if (ydiff - ydiff.iloc[0]).sum() == 0:
                y_found = True
                yo = - ydiff.iloc[0]
                comp_matches['y'] = -comp_matches['y']-yo
                comp_beacon['y'] = -comp_beacon['y']-yo
                
    zdiff = zb_matches['z'] - comp_matches['z']
    if (zdiff - zdiff.iloc[0]).sum() == 0:
        zo = zdiff.iloc[0]
        comp_matches['z'] = comp_matches['z']+zo
        comp_beacon['z'] = comp_beacon['z']+zo
    else:
        zdiff = zb_matches['z'] + comp_matches['z']
        if (zdiff - zdiff.iloc[0]).sum() == 0:
            zo = - zdiff.iloc[0]
            comp_matches['z'] = -comp_matches['z']-zo
            comp_beacon['z'] = -comp_beacon['z']-zo
        else:
            print('Logic error: Rotation not found')
            
    rot_beacons.append(comp_beacon)
            
            
            
                
    # print('Finished rotation')
    
    #Rotation:
    #y z
    #----
    #y z
    #z -y
    #-y -z
    #-z y
    #Then invert x and repeat
    # then cycle x to y and z
