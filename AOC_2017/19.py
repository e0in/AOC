# -*- coding: utf-8 -*-
"""
Created on Sat May  6 23:48:42 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# [fname] = ["19_test.txt"]
[fname] = ["19.txt"]

# packet = np.loadtxt(fname, dtype = "str")

with open(fname, 'r') as file:
    packet = file.read().splitlines()

w = len(packet[0])
h = len(packet)

packet = [list(x) for x in packet]

x_0 = packet[0].index('|')

arr = np.array(packet)
pad_arr = np.pad(arr, 1, mode='constant', constant_values=" ")

[y, x] = [1, x_0+1]
# dyx = [1, 0]
dy = 1
dx = 0

letters = []

can_cont = True

count = 0

while can_cont:
    count += 1
    y += dy
    x += dx
    
    val = str(pad_arr[y, x])
    
    if val == "|" or val == "-":
        continue
    elif val == "+":
        [dy, dx] = [dx, dy]
        if pad_arr[y + dy, x + dx] == " ":
            [dy, dx] = [-dy, -dx]
    elif val == " ":
        can_cont = False
    else:
        letters.append(val)

print(f'Answer 1 is {"".join(letters)}')

print(f'Answer 2 is {count}')