# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:34:29 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd


test = "()())"
with open('1_1.txt', 'r') as file:
    input1 = file.read().rstrip()

ans = input1.count("(") - input1.count(")")

print(f'Answer 1 is {ans}')

# %% Part 2

curfloor = 0

for i in range(len(input1)):
    if input1[i] == "(":
        curfloor += 1
    else:
        curfloor -= 1
    
    if curfloor == -1:
        break

print(f'Answer 2 is {i+1}')