# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 22:15:21 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

import hashlib

# salt = 'abc'
salt = 'yjdafjpo'
    
triple = {'0':[], '1':[], '2':[], '3':[], '4':[], '5':[],
          '6':[], '7':[], '8':[], '9':[], 'a':[], 'b':[],
          'c':[], 'd':[], 'e':[], 'f':[]}

quint =  {'0':[], '1':[], '2':[], '3':[], '4':[], '5':[],
          '6':[], '7':[], '8':[], '9':[], 'a':[], 'b':[],
          'c':[], 'd':[], 'e':[], 'f':[]}

i = 0
# while i < 40000:
#     s_hash = salt + str(i)
    
#     s_str = hashlib.md5(s_hash.encode('utf-8')).hexdigest()
    
#     triple_found = False
    
#     for j in range(0, 28):
#         if s_str[j] == s_str[j+1] == s_str[j+2] == s_str[j+3] == s_str[j+4]:
#             quint[s_str[j]].append(i)
                
                
#     for j in range(0, 30):
#         if not triple_found:
#             if s_str[j] == s_str[j+1] == s_str[j+2]:
#                 triple[s_str[j]].append(i)
#                 triple_found = True
    
#     i += 1
    
# valid = set()
    
# for key in triple.keys():
#     arr = np.array(triple[key])
#     for q in quint[key]:
#         valid = valid.union(set(arr[np.logical_and((q-1000 <= arr), (arr < q))]))
        
# valid = sorted(list(valid))

# print(f"Answer 1 is {valid[63]}")

    
triple = {'0':[], '1':[], '2':[], '3':[], '4':[], '5':[],
          '6':[], '7':[], '8':[], '9':[], 'a':[], 'b':[],
          'c':[], 'd':[], 'e':[], 'f':[]}

quint =  {'0':[], '1':[], '2':[], '3':[], '4':[], '5':[],
          '6':[], '7':[], '8':[], '9':[], 'a':[], 'b':[],
          'c':[], 'd':[], 'e':[], 'f':[]}

keys_found = 0

i = 0

while i < 30000:
    s_hash = salt + str(i)
    
    s_str = hashlib.md5(s_hash.encode('utf-8')).hexdigest()
    for _ in range(2016):
        s_str = hashlib.md5(s_str.encode('utf-8')).hexdigest()
    
    triple_found = False
    
    for j in range(0, 28):
        if s_str[j] == s_str[j+1] == s_str[j+2] == s_str[j+3] == s_str[j+4]:
            quint[s_str[j]].append(i)
                
                
    for j in range(0, 30):
        if not triple_found:
            if s_str[j] == s_str[j+1] == s_str[j+2]:
                triple[s_str[j]].append(i)
                triple_found = True
    
    i += 1
    
valid = set()
    
for key in triple.keys():
    arr = np.array(triple[key])
    for q in quint[key]:
        valid = valid.union(set(arr[np.logical_and((q-1000 <= arr), (arr < q))]))

valid = sorted(list(valid))

print(f"Answer 2 is {valid[63]}")
