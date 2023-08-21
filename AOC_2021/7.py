# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:15:13 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

test = pd.Series("16,1,2,0,4,2,7,1,2,14".split(',')).astype(int)
input7 = pd.read_csv("7.txt", sep=",", header=None, dtype="int",
                     engine='python').squeeze()

# # Selector, put True for test data
# if False:
#     df = test
#     ndays = 18 #ans1 = 26
#     #ndays = 80 #5934
# else:
#     df = input6.copy()
#     ndays = 80
    
# minvalue = 1000000

# for i in range(300, 500):
#     if (input7 - i).abs().sum() < minvalue:
#         minvalue = (input7 - i).abs().sum()
#     #print(df)
    
    
print(f'Answer 1 is {(input7 - int(input7.median())).abs().sum()}')

minvalue2 = 100000000

for i in range(int(input7.mean())-1, int(input7.mean())+1):
    dist = (input7 - i).abs()
    fuel = int((dist * (dist+1)).sum()/2)
    if fuel < minvalue2:
        minvalue2 = fuel
    #print(df)


print(f'Answer 2 is {minvalue2}')