# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:54:55 2021

@author: Eoin
"""

import math
import numpy as np
import pandas as pd

test1 = pd.read_csv("12_test_1.txt", sep="-", header=None, engine = 'python')
test2 = pd.read_csv("12_test_2.txt", sep="-", header=None, engine = 'python')
test3 = pd.read_csv("12_test_3.txt", sep="-", header=None, engine = 'python')
input12 = pd.read_csv("12.txt", sep="-", header=None, engine = 'python')

# Change to True for test data, False for real
data = 1
if data == 1:
    df = test1
elif data == 2:
    df = test2
elif data == 3:
    df = test3
else:
    df = input12
    
valid_paths = [["start"]]


while len([path[-1] for path in valid_paths if path[-1] != 'end']) > 0:
    for path in [p for p in valid_paths if p[-1] != 'end']:
        conn = df[(df == path[-1]).any(axis=1)]
        conn = conn[conn != path[-1]].stack().reset_index(drop=True).tolist()
        low_caves = [c for c in path if c.islower()]
        valid_conn = [elem for elem in conn if elem not in low_caves]
        
        valid_paths.remove(path)
        if len(valid_conn) > 0:
            for dest in valid_conn:
                valid_paths.append(path + [dest])
                    
print(f'Answer 1 is {len(valid_paths)}')

valid_paths = [["start"]]

while len([path[-1] for path in valid_paths if path[-1] != 'end']) > 0:
    for path in [p for p in valid_paths if p[-1] != 'end']:
        conn = df[(df == path[-1]).any(axis=1)]
        conn = conn[conn != path[-1]].stack().reset_index(drop=True).tolist()
        
        low_list = [c for c in path if c.islower()]
        if len(low_list) == len(set(low_list)):
            low_caves = [c for c in path if c.islower() and path.count(c) > 1] + ['start']
        else:
            low_caves = low_list
        
        
        valid_conn = [elem for elem in conn if elem not in low_caves]
        
        valid_paths.remove(path)
        if len(valid_conn) > 0:
            for dest in valid_conn:
                valid_paths.append(path + [dest])

print(f'Answer 2 is {len(valid_paths)}')