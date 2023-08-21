# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:42:16 2023

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from collections import defaultdict

turn = defaultdict(lambda: 0)

seq = [0,3,6]
for i in range(len(seq)):
    turn[seq[i]] = i+1

seq.append(0)
n = len(seq)

for i in range(n+1, 10+1):
    if turn[seq[-1]] == 0:
        turn[seq[-1]] = i-1
        seq.append(0)
        

# print(f'Answer 2 is {sum(memv2.values())}')