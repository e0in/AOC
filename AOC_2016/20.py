# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 21:17:47 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

ip = pd.read_csv("20.txt", sep="-", header=None, names = ["low", "high"], engine='python')
ip.sort_values('low', inplace=True, ignore_index=True)

test0 = pd.DataFrame([[0, 2], [4, 7], [5,8]], columns=["low", "high"])

test1 = pd.DataFrame([[0, 200], [4, 7], [190,300], [305, 420], [400, 450]], columns=["low", "high"])

def min_valid(ip):
    low_ban = 0
    
    for i in range(len(ip)):
        if low_ban < ip.loc[i, 'low']-1:
            break
        elif low_ban < ip.loc[i, 'high']:
            low_ban = ip.loc[i, 'high']
    return low_ban + 1
    

assert min_valid(test1) == 301

print(f"Answer 1 is {min_valid(ip)}")

def valid_count(ip, i_max=4294967296):
    subs = []
    clean_ip = ip.copy()
    
    for i in range(1, len(clean_ip)):
        for j in range(0, i):
            if (clean_ip.loc[i, 'low'] < clean_ip.loc[j, 'high']) and (clean_ip.loc[i, 'high'] <= clean_ip.loc[j, 'high']):
                subs.append(i)
    
    clean_ip.drop(subs, axis=0, inplace=True)
    clean_ip.reset_index(inplace=True, drop=True)
    
    for i in range(1, len(clean_ip)):
        if clean_ip.loc[i, 'low'] < clean_ip.loc[:i-1, 'high'].max():
            clean_ip.loc[i, 'low'] = clean_ip.loc[:i-1, 'high'].max() + 1
    
    clean_ip['nban'] = clean_ip['high'] - clean_ip['low'] + 1
    
    return clean_ip, i_max - (clean_ip['nban'].sum())
    
    #return i_max - (ip['nban'].sum())

#print(valid_count(test1, i_max=450))
assert valid_count(test0, i_max=10)[1] == 2

vals = valid_count(test0, i_max=9)[0]

print(f"Answer 2 is {valid_count(ip)[1]}")
