# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 14:14:22 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd


test = pd.read_csv("7_test.txt", sep=" -> ", header=None, dtype="str",
                   engine='python', names = ['inst', 'wire'])
input3 = pd.read_csv("7.txt", sep=" -> ", header=None, dtype="str",
                     engine='python', names = ['inst', 'wire'])
test['exec'] = False
input3['exec'] = False

testwires = pd.DataFrame(data={'wire':test['wire'], 'val':np.nan}).sort_values('wire')
wires = pd.DataFrame(data={'wire':input3['wire'], 'val':np.nan}).sort_values('wire')

for i in range(len(test)):
    if test.iloc[i,0].isnumeric():
        n = int(test.iloc[i,0])
        testwires.loc[testwires['wire'] == test.iloc[i, 1], 'val'] = n
        test.iloc[i, 2] = True

test = test[~test['exec']]

test_ops = test['inst'].str.split(expand = True)
test_nots = (test_ops[0] == 'NOT')
test_ops.loc[test_nots, [0,2]] = test_ops.loc[test_nots, 1]
test_ops.loc[test_nots, 1] = 'NOT'
test_ops.rename(columns={0: "w1", 1: "op", 2: 'w2'}, inplace = True)

test = pd.concat([test, test_ops], axis= 1)

while (len(test) > 0):
    for i in range(len(test)):
        w1 = test.iloc[i,3]
        v1 = testwires.loc[testwires['wire'] == w1, 'val']
        w2 = test.iloc[i,5]
        v2 = testwires.loc[testwires['wire'] == w2, 'val']
        
        if (v1.isna()) or (v2.isna()):
            continue
        
        
        v1 = v1.squeeze()
        v2 = v2.squeeze()
        
        op = test.iloc[i,4]
        
        if op = 'NOT':
        
        
        
        
        
        
        test.iloc[i, 2] = True # mark operation as executed
    
    test = test[~test['exec']]