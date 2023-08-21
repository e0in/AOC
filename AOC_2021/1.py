# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:00:57 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

inputtest = np.array([199,200,208,210,200,207,240,269,260,263])
input1 = np.loadtxt("1_1.txt")

diff = np.diff(input1)

print(f'Answer 1 is {sum(diff> 0)}')

# %% Part 2

sum3 = np.convolve(input1, np.ones(3,dtype=int), 'valid')

diff2 = np.diff(sum3)

print(f'Answer 2 is {sum(diff2> 0)}')