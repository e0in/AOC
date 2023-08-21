# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 11:31:36 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

test = pd.read_csv("10_test.txt", header=None, dtype = "str")
input10 = pd.read_csv("10.txt", header=None, dtype = "str")

# Selector, put True for test data
if False:
    df = test
else:
    df = input10
    
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
total = 0
df[1] = False
    
def bracket_remove(input_str):
    out_str = input_str.replace('()', '')
    out_str = out_str.replace('[]', '')
    out_str = out_str.replace('{}', '')
    out_str = out_str.replace('<>', '')
    return(out_str)

for i in range(len(df)):
    n1 = 0
    n2 = len(df[0][i])
    
    while (n1 != n2):
        n1 = n2
        df.loc[i, 0] = bracket_remove(df.loc[i, 0])
        n2 = len(df[0][i])
    
    fin = df[0][i]
    mins = [fin.find(')'), fin.find(']'), fin.find('}'), fin.find('>')]
    mins = list(filter(lambda a: a != -1, mins))
    
    if len(mins) > 0:
        illegal_char = fin[min(mins)]
        total += points[illegal_char]
    else:
        df.loc[i, 1] = True
        
print(f'Answer 1 is {total}') 

incomp = df.loc[df[1], 0].reset_index(drop=True)
totals2 = []
points2 = {'(': 1, '[': 2, '{': 3, '<': 4}

for i in range(len(incomp)):
    comp_val = 0
    in_str = incomp[i]
    for j in range(len(in_str)-1, -1, -1):
        comp_val *= 5
        comp_val += points2[in_str[j]]
    
    totals2.append(comp_val)
    
print(f'Answer 2 is {int(pd.Series(totals2).median())}') 