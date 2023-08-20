# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:42:39 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest


def get_prio(c):
    #df = pd.read_csv(fname, header=None, engine='python')
    try:
        if math.isnan(c):
            return 0
    except:
        val = ord(c)
        
        if val >= 97:
            return(val-96)
        else:
            return(val-38)

assert get_prio("a") == 1
assert get_prio("z") == 26
assert get_prio("A") == 27
assert get_prio("Z") == 52


test = pd.read_csv("3_test.txt", header=None, names = ["full"], engine='python')
ruck = pd.read_csv("3.txt", header=None, names = ["full"], engine='python')

if True: # selector, True for full data
    df = ruck
else:
    df = test

for i in range(len(df)):
    s = df.loc[i, "full"]
    l = len(s)
    s1 = s[:l//2]
    s2 = s[l//2:]
    
    df.loc[i,"s1"] = s1
    df.loc[i,"s2"] = s2
    
    df.loc[i,"common"] = ''.join(set(s1).intersection(s2))
    df.loc[i,"prio"] = get_prio(df.loc[i,"common"])
    
print(f"Answer 1 is {int(df['prio'].sum())}")


for i in range(0, len(df), 3):
    s1 = df.loc[i, "full"]
    s2 = df.loc[i+1, "full"]
    s3 = df.loc[i+2, "full"]
    
    df.loc[i, "badge"] = ''.join(set(s1).intersection(s2).intersection(s3))
    
df['b_prio'] = df['badge'].apply(get_prio)

print(f"Answer 1 is {int(df['b_prio'].sum())}")