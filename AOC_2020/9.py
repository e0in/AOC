# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 19:01:38 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest


def preamble(fname, pre):
    #df = pd.read_csv(fname, header=None, engine='python')
    xmas = np.loadtxt(fname, dtype = "double")
    
    i = 0
    Found = True
    ret_val = 0
    
    while Found:
        Found = False
        #cur = df[i:i+pre]
        for j in range(i,i+pre-1):
            for k in range(j+1,i+pre):
                #print(i, j, k)
                if xmas[i+pre] == xmas[j] + xmas[k]:
                    Found = True
                    #print(f"Found, {i, j, k, xmas[i+pre], xmas[j], xmas[k]}")
        
        i += 1
        
    return(xmas[i+pre-1])

assert preamble("9_test.txt", 5) == 127

ans1 = preamble("9.txt", 25)

print(f"Answer 1 is {ans1}")

def contig(fname, trgt):
    xmas = np.loadtxt(fname, dtype = "double")
    
    cur = 0
    i = 0
    j=1
    
    for i in range(len(xmas)-1):
        for j in range(i+1,len(xmas)):
            cur = xmas[i:j+1].sum()
            if cur == trgt:
                return(xmas[i:j+1].min() + xmas[i:j+1].max())


assert contig("9_test.txt", 127) == 62

ans2 = contig("9.txt", 15690279)

print(f"Answer 2 is {ans2}")