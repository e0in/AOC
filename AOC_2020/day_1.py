# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:07:16 2020

@author: Eoin
"""

import math
import numpy as np
import pandas as pd

data = np.loadtxt("C:\Python\AOC_2020\input1", dtype = "int")

i = 0 # First number
j = 1 # Second num
k = 2 # Third number
ans = 0 # answer

for i in range(len(data)-2):
    for j in range(1, len(data) - 1):
        for k in range(2, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                ans = data[i] * data[j] * data[k]
        