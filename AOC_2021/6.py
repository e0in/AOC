# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:57:49 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import tqdm

test = pd.Series("3,4,3,1,2".split(',')).astype(int)
input6 = pd.read_csv("6.txt", sep=",", header=None, dtype="int",
                     engine='python').squeeze()

# # Selector, put True for test data
# if False:
#     df = test
#     ndays = 18 #ans1 = 26
#     #ndays = 80 #5934
# else:
#     df = input6.copy()
#     ndays = 80
    

# for i in range(ndays):
#     breeding = (df == 0)
#     df -= 1
#     df[breeding] = 6
#     df = df.append(pd.Series([8]*breeding.sum(), dtype=int), ignore_index=True)
    
#     #print(df)
    
    
# print(f'Answer 1 is {len(df)}')

# Original too slow, solution stolen from reddit
data = input6.tolist()
fish = [data.count(i) for i in range(9)]

for i in range(256):
    num = fish.pop(0)
    fish[6] += num
    fish.append(num)
    assert len(fish) == 9


print(f'Answer 2 is {sum(fish)}')