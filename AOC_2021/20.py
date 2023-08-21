# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:19:01 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

test = pd.read_csv("20_test.txt", sep='\n\n', header=None, engine='python')
inputdat = pd.read_csv("20.txt", sep='\n\n', header=None, engine='python')

# Selector, put True for test data
if False:
    df = test
else:
    df = inputdat

df[0] = df[0].str.replace('#', '1').str.replace('.', '0')

inst = df[0][0]# .replace('#', '1')

df.drop(0, inplace=True) 
df.reset_index(drop=True, inplace=True)
df = df[0].apply(lambda x: pd.Series(list(x))) #.astype(int)

def im_enhance(df, inst, n_iter=1, inf_on=False):
    
    if inf_on and (inst[0] == '1'):
        pad_df = pd.DataFrame(np.pad(df, 2, constant_values='1'), dtype=str)
    else:
        pad_df = pd.DataFrame(np.pad(df, 2, constant_values='0'), dtype=str)
    df_out = pd.DataFrame(np.zeros([df.shape[0]+1, df.shape[1]+1], dtype=str))
    
    for i in range(1, pad_df.shape[0]-1):
        for j in range(1, pad_df.shape[1]-1):
            fil = pad_df.loc[i-1:i+1, j-1:j+1]
            bin_str = ''.join(fil.stack().tolist())
            ind = int(bin_str, 2)
            df_out.loc[i-1, j-1] = inst[ind]
            
    
    n_iter -= 1
    inf_on = not inf_on
    if n_iter == 0:
        return(df_out)
    else:
        print(f'{n_iter} iterations to go')
        return(im_enhance(df_out, inst, n_iter, inf_on))
    
df_out = im_enhance(df, inst, 2)
#plt.imshow(df_out.astype(int))

print(f'Answer 1 is {df_out.astype(int).sum().sum()}')

df_out2 = im_enhance(df, inst, 50)
#plt.imshow(df_out.astype(int))

print(f'Answer 2 is {df_out2.astype(int).sum().sum()}')