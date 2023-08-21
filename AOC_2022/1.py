# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:46:48 2022

@author: ehorgan
"""

#import math
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt

# test = pd.read_csv("1_test.txt", sep='\n\n', header=None, engine='python')
# inputdat = pd.read_csv("1.txt", sep='\n\n', header=None, engine='python')

# # Selector, put True for test data
# if True:
#     df = test
# else:
#     df = inputdat

with open('1.txt', 'r') as f:  
# with open('1_test.txt', 'r') as f:
    food = f.readlines()

cals = []
cur = 0

for elem in food:
    if elem == '\n':
        cals.append(cur)
        cur=0
    else:
        cur += int(elem)
cals.append(cur)

print(f'Answer 1 is {max(cals)}')

cals.sort()

print(f'Answer 2 is {sum(cals[-3:])}')