# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:36:27 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

#manually edited to have two spaces after every toggle
input6 = pd.read_csv("6.txt", sep=" ", header=None,
                     names = ["remove", "inst", "coord1", "remove2", "coord2"])

input6.loc[input6.loc[:, "inst"].isna(), "inst"] = "toggle"

input6[['x1', 'y1']] = input6["coord1"].str.split(',', 2, expand = True)
input6[['x2', 'y2']] = input6["coord2"].str.split(',', 2, expand = True)

input6.drop(["remove", "coord1", "remove2", "coord2"], axis=1, inplace = True)

lights = np.zeros([1000, 1000], dtype="bool")

for i in range(len(input6)):
    [x1, y1, x2, y2] = input6.loc[i, "x1":"y2"].astype(int) # convert to int
    if input6.loc[i, "inst"] == "on":
        lights[y1:y2+1, x1:x2+1] = True
    elif input6.loc[i, "inst"] == "off":
        lights[y1:y2+1, x1:x2+1] = False
    else:
        lights[y1:y2+1, x1:x2+1] = ~lights[y1:y2+1, x1:x2+1]
        

print(f'Answer 1 is {lights.sum()}')

# %% Part 2


lights = np.zeros([1000, 1000], dtype="int")

for i in range(len(input6)):
    [x1, y1, x2, y2] = input6.loc[i, "x1":"y2"].astype(int) # convert to int
    if input6.loc[i, "inst"] == "on":
        lights[y1:y2+1, x1:x2+1] = lights[y1:y2+1, x1:x2+1] + 1
    elif input6.loc[i, "inst"] == "off":
        lights[y1:y2+1, x1:x2+1] = lights[y1:y2+1, x1:x2+1] - 1
        lights[lights < 0] = 0
    else:
        lights[y1:y2+1, x1:x2+1] = lights[y1:y2+1, x1:x2+1] + 2
        
        
print(f'Answer 2 is {lights.sum()}')
