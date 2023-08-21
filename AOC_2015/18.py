# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 15:05:41 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

test = pd.read_csv("18_test.txt", sep='\n\n', header=None, engine='python')
inputdat = pd.read_csv("18.txt", sep='\n\n', header=None, engine='python')

# Selector, put True for test data
if False:
    df = test
else:
    df = inputdat

df[0] = df[0].str.replace('#', '1').str.replace('.', '0')
df = df[0].apply(lambda x: pd.Series(list(x))).astype(int)
[L, W] = df.shape

df = np.pad(df, 1, constant_values=0)
df2 = df.copy()

def im_anim(df, L, W, n_iter=1, corners=False):
    df_out = df.copy()
    
    for i in range(1, W+1):
        for j in range(1, L+1):
            fil = df[i-1:i+2, j-1:j+2]
            n = fil.sum()
            
            light_works = True
            
            if corners:
                if (i, j) in [(1, 1), (L, 1), (1, W), (L, W)]:
                    light_works = False
            
            
            if light_works:
                if df[i, j]:
                    if (n < 3) or (n > 4):
                        df_out[i, j] = 0
                else:
                    if n == 3:
                        df_out[i, j] = 1
            
    n_iter -= 1
    if n_iter == 0:
        return(df_out)
    else:
        print(f'{n_iter} iterations to go')
        return(im_anim(df_out, L, W, n_iter, corners=corners))
    
# 4 for test, 100 for real
ans1 = im_anim(df, L, W, n_iter=100)

print(f'Answer 1 is {ans1.sum()}')

[df2[1, 1], df2[L, 1], df2[1, W], df2[L, W]] = [1, 1, 1, 1]


ans2 = im_anim(df2, L, W, n_iter=100, corners=True)
# #plt.imshow(df_out.astype(int))

print(f'Answer 2 is {ans2.sum()}')