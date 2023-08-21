# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:15:01 2023

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

# [fname] = ["14_test.txt"]
# [fname] = ["14_test2.txt"]
[fname] = ["14.txt"]

with open(fname, 'r') as file:
    inst = file.read().splitlines()

mem = defaultdict(lambda: 0)

mask = np.array(list('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'))

# for line in inst:
#     if line[:6] == 'mask =':
#         mask = np.array(list(line[7:]))
#     else:
#         [tmp, init_val] = line.split('] = ')
#         [_, dest] = tmp.split('[')
#         dest = int(dest)
        
#         bin_rep = np.array(list(format(int(init_val), '036b')))
        
#         bin_rep[mask == '1'] = '1'
#         bin_rep[mask == '0'] = '0'
        
#         new_val = int(''.join(list(bin_rep)), 2)
        
#         mem[dest] = new_val
    
# print(f'Answer 1 is {sum(mem.values())}')

memv2 = defaultdict(lambda: 0)

for line in inst:
    if line[:6] == 'mask =':
        mask = np.array(list(line[7:]))
    else:
        [tmp, val] = line.split('] = ')
        [_, dest] = tmp.split('[')
        dest = int(dest)
        
        bin_rep = np.array(list(format(int(dest), '036b')))
        
        bin_rep[mask == '1'] = '1'
        bin_rep[mask == 'X'] = 'X'

        Q = [bin_rep]
        
        while Q:
            curr = Q.pop()
            
            if ''.join(list(curr)).isnumeric():
                memv2[int(''.join(list(curr)), 2)] = int(val)
            else:
                ind = np.where(curr == 'X')[0][0]
                curr[ind] = '0'
                Q.append(curr)
                next_ver = curr.copy()
                next_ver[ind] = '1'
                Q.append(next_ver)
        

print(f'Answer 2 is {sum(memv2.values())}')
