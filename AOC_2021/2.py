# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:34:29 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

#test = np.genfromtxt("2_test.txt")
#input2 = np.genfromtxt("2_1.txt")

test = pd.read_csv("2_test.txt", sep=" ", header=None, names = ["dir", "mag"])
input2 = pd.read_csv("2_1.txt", sep=" ", header=None, names = ["dir", "mag"])

hor = input2.loc[input2["dir"] == "forward", "mag"].sum()

up = input2.loc[input2["dir"] == "up", "mag"].sum()
down = input2.loc[input2["dir"] == "down", "mag"].sum()
depth = down - up


print(f'Answer 1 is {depth * hor}')

# %% Part 2

aim = 0
hor = 0
depth = 0

for i in range(len(input2)):
    if input2.iloc[i,0] == "down":
        aim += input2.iloc[i, 1]
    elif input2.iloc[i,0] == "up":
        aim -= input2.iloc[i, 1]
    else:
        hor += input2.iloc[i, 1]
        depth += (aim * input2.iloc[i, 1])
        
    #print([aim, hor, depth])

print(f'Answer 2 is {depth * hor}')