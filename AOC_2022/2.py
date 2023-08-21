# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:46:48 2022

@author: ehorgan
"""

#import math
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

test = pd.read_csv("2_test.txt", sep=' ', header=None, engine='python', names = ["opp", "you"])
inputdat = pd.read_csv("2.txt", sep=' ', header=None, engine='python', names = ["opp", "you"])

# Selector, put True for test data
if False:
    df = test
else:
    df = inputdat

df.replace(['A', 'B', 'C'], [1,2,3], inplace=True)
df.replace(['X', 'Y', 'Z'], [1,2,3], inplace=True)
#df['gr'] = df['you'] > df['opp']
#df['eq'] = df['you'] == df['opp']
df['diff'] = df['you'] - df['opp']
df['score'] = df['diff']

df['score'].replace([1, -2], [6, 6], inplace=True)
df['score'].replace(0, 3, inplace=True)
df['score'].replace([-1, 2], [0, 0], inplace=True)

df['score'] = df['score'] + df['you']


print(f'Answer 1 is {df["score"].sum()}')

df['win'] = df['opp']%3+1
df['draw'] = df['opp']
df['lose'] = (df['opp']-1) + 3*(df['opp']==1)

df['resp'] = df['you']

for i in range(len(df)):
    cond = df.loc[i, 'resp']
    
    if cond == 3:
        df.loc[i, 'resp'] = df.loc[i, 'win']
    elif cond == 2:
        df.loc[i, 'resp'] = df.loc[i, 'draw']
    else:
        df.loc[i, 'resp'] = df.loc[i, 'lose']
    
#df['win'][df['you']==3] + df['draw'][df['you']==2] + df['lose'][df['you']==1]

df['diff2'] = df['resp'] - df['opp']
df['score2'] = df['diff2']

df['score2'].replace([1, -2], [6, 6], inplace=True)
df['score2'].replace(0, 3, inplace=True)
df['score2'].replace([-1, 2], [0, 0], inplace=True)

df['score2'] = df['score2'] + df['resp']


print(f'Answer 1 is {df["score2"].sum()}')