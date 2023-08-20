# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 10:24:58 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

with open('10.txt', 'r') as file:
    inst = file.read().splitlines()

# with open('10_test.txt', 'r') as file:
# with open('10_test2.txt', 'r') as file:
#     inst = file.read().splitlines()

inst = [x.split() for x in inst]

signal = []
x = 1

for line in inst:
    if line[0] == 'noop':
        signal.append(x)
    elif line[0] == 'addx':
        signal.append(x)
        signal.append(x)
        x += int(line[1])
    #print(x, signal)
strength = 0

for i in range(20, 221, 40):
    strength += i * signal[i-1]
    

print(f"Answer 1 is {strength}")

sig_arr = np.array(signal)
sig_arr_m = sig_arr - 1
sig_arr_p = sig_arr + 1
crt_pos = np.tile(np.arange(40), 6) # np.arange(240)

pix = (crt_pos == sig_arr) + (crt_pos == sig_arr_m) + (crt_pos == sig_arr_p)

img = pix.reshape(6, 40)

plt.imshow(img) # ANS = BUCACBUZ

