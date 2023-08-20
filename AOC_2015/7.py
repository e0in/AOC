# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:39:49 2021

@author: Eoin
"""

import math
import numpy as np
import pandas as pd


test = pd.read_csv("7_test.txt", sep=" -> ", header=None, dtype="str",
                   engine='python', names = ['inst', 'wire'])
input7 = pd.read_csv("7.txt", sep=" -> ", header=None, dtype="str",
                     engine='python', names = ['inst', 'wire'])
test['exec'] = False
input7['exec'] = False

testwires = pd.DataFrame(data={'wire':test['wire'], 'val':np.nan}).sort_values('wire')
wires = pd.DataFrame(data={'wire':input7['wire'], 'val':np.nan}).sort_values('wire')


#%% Test data section 
# for i in range(len(test)):
#     if test.iloc[i,0].isnumeric():
#         n = int(test.iloc[i,0])
#         testwires.loc[testwires['wire'] == test.iloc[i, 1], 'val'] = n
#         test.iloc[i, 2] = True

# test = test[~test['exec']]

# test_ops = test['inst'].str.split(expand = True)
# test_nots = (test_ops[0] == 'NOT')
# test_ops.loc[test_nots, [0,2]] = test_ops.loc[test_nots, 1]
# test_ops.loc[test_nots, 1] = 'NOT'
# test_ops.rename(columns={0: "w1", 1: "op", 2: 'w2'}, inplace = True)

# test = pd.concat([test, test_ops], axis= 1)

# while (len(test) > 0):
#     for i in range(len(test)):
#         w1 = test.iloc[i,3]
#         v1 = testwires.loc[testwires['wire'] == w1, 'val']
#         w2 = test.iloc[i,5]
#         v2 = testwires.loc[testwires['wire'] == w2, 'val']
        
#         if (v1.isna().squeeze()):
#             continue
        
#         PASS2 = False
        
#         if w2.isnumeric():
#             PASS2 = True

#         if (not PASS2):
#             if (v2.isna().squeeze()):
#                 continue

        
#         dest = test.iloc[i, 1]
#         v1 = int(v1.squeeze())
        
#         op = test.iloc[i,4]
        
#         if op == 'NOT':
#             out = v1 ^ 65535
#         elif op == 'AND':
#             v2 = int(v2.squeeze())
#             out = v1 & v2
#         elif op == 'OR':
#             v2 = int(v2.squeeze())
#             out = v1 | v2
#         elif op == 'LSHIFT':
#             w2 = int(w2)
#             out = v1 << w2
#         else:
#             w2 = int(w2)
#             out = v1 >> w2
        
#         testwires.loc[testwires['wire'] == dest, 'val'] = out
#         test.iloc[i, 2] = True # mark operation as executed
    
#     test = test[~test['exec']]
    
    
#%% Real data section
    
    
for i in range(len(input7)):
    if input7.iloc[i,0].isnumeric():
        n = int(input7.iloc[i,0])
        wires.loc[wires['wire'] == input7.iloc[i, 1], 'val'] = n
        input7.iloc[i, 2] = True

input7 = input7[~input7['exec']]

input7_ops = input7['inst'].str.split(expand = True)
input7_nots = (input7_ops[0] == 'NOT')
input7_ops.loc[input7_nots, [0,2]] = input7_ops.loc[input7_nots, 1]
input7_ops.loc[input7_nots, 1] = 'NOT'
input7_ops.rename(columns={0: "w1", 1: "op", 2: 'w2'}, inplace = True)

input7 = pd.concat([input7, input7_ops], axis= 1)

while (len(input7) > 0):
    for i in range(len(input7)):
        dest = input7.iloc[i, 1]
        op = input7.iloc[i,4]
        
        w1 = input7.iloc[i,3]
        PASS1 = False
        
        if w1.isnumeric():
            PASS1 = True
            v1 = int(w1)
        else:
            v1 = wires.loc[wires['wire'] == w1, 'val']
            if (v1.isna().squeeze()):
                continue

        w2 = input7.iloc[i,5]
        PASS2 = False
        
        if w2 == None: # no op, lx to a
            wires.loc[wires['wire'] == dest, 'val'] = int(v1.squeeze())
            input7.iloc[i, 2] = True # mark operation as executed
            continue
        
        if w2.isnumeric():
            PASS2 = True
            v2 = int(w2)
        else:
            v2 = wires.loc[wires['wire'] == w2, 'val']
            if (v2.isna().squeeze()):
                continue
        
        if (not isinstance(v1, int)):
            v1 = int(v1.squeeze())
        if (not isinstance(v2, int)):
            v2 = int(v2.squeeze())
       
        
        if op == 'NOT':
            out = v1 ^ 65535
        elif op == 'AND':
            out = v1 & v2
        elif op == 'OR':
            out = v1 | v2
        elif op == 'LSHIFT':
            out = v1 << v2
        elif op == 'RSHIFT':
            out = v1 >> v2
        
        wires.loc[wires['wire'] == dest, 'val'] = out
        input7.iloc[i, 2] = True # mark operation as executed
    
    input7 = input7[~input7['exec']]

ans1 = int(wires.loc[wires['wire'] == 'a', 'val'])
    
print(f'Answer 1 is {ans1}')


#%% Part 2

wires['val'] = np.nan

input7 = pd.read_csv("7_2.txt", sep=" -> ", header=None, dtype="str",
                     engine='python', names = ['inst', 'wire'])
input7['exec'] = False

for i in range(len(input7)):
    if input7.iloc[i,0].isnumeric():
        n = int(input7.iloc[i,0])
        wires.loc[wires['wire'] == input7.iloc[i, 1], 'val'] = n
        input7.iloc[i, 2] = True

input7 = input7[~input7['exec']]

input7_ops = input7['inst'].str.split(expand = True)
input7_nots = (input7_ops[0] == 'NOT')
input7_ops.loc[input7_nots, [0,2]] = input7_ops.loc[input7_nots, 1]
input7_ops.loc[input7_nots, 1] = 'NOT'
input7_ops.rename(columns={0: "w1", 1: "op", 2: 'w2'}, inplace = True)

input7 = pd.concat([input7, input7_ops], axis= 1)

while (len(input7) > 0):
    for i in range(len(input7)):
        dest = input7.iloc[i, 1]
        op = input7.iloc[i,4]
        
        w1 = input7.iloc[i,3]
        PASS1 = False
        
        if w1.isnumeric():
            PASS1 = True
            v1 = int(w1)
        else:
            v1 = wires.loc[wires['wire'] == w1, 'val']
            if (v1.isna().squeeze()):
                continue

        w2 = input7.iloc[i,5]
        PASS2 = False
        
        if w2 == None: # no op, lx to a
            wires.loc[wires['wire'] == dest, 'val'] = int(v1.squeeze())
            input7.iloc[i, 2] = True # mark operation as executed
            continue
        
        if w2.isnumeric():
            PASS2 = True
            v2 = int(w2)
        else:
            v2 = wires.loc[wires['wire'] == w2, 'val']
            if (v2.isna().squeeze()):
                continue
        
        if (not isinstance(v1, int)):
            v1 = int(v1.squeeze())
        if (not isinstance(v2, int)):
            v2 = int(v2.squeeze())
       
        
        if op == 'NOT':
            out = v1 ^ 65535
        elif op == 'AND':
            out = v1 & v2
        elif op == 'OR':
            out = v1 | v2
        elif op == 'LSHIFT':
            out = v1 << v2
        elif op == 'RSHIFT':
            out = v1 >> v2
        
        wires.loc[wires['wire'] == dest, 'val'] = out
        input7.iloc[i, 2] = True # mark operation as executed
    
    input7 = input7[~input7['exec']]

ans2 = int(wires.loc[wires['wire'] == 'a', 'val'])
    
print(f'Answer 2 is {ans2}')