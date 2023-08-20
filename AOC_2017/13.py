# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 14:51:41 2023

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

[fname] = ["13_test.txt"]
[fname] = ["13.txt"]

with open(fname, "r") as file:
    wall = file.read().splitlines()

fwall = []
for line in wall:
    [a, b] = line.split(': ')
    fwall.append([int(a), int(b), (int(b)-1)*2])

severity = 0

for line in fwall:
    [a, b, _] = line
    period = (b-1)*2
    
    if a%period == 0:
        severity += a*b


print(f'Answer 1 is {severity}')

t_delay = 0
while severity  > 0:
    t_delay += 1
    
    severity = 0
    
    for line in fwall:
        [a, b, c] = line
        
        if (a+t_delay)%c == 0:
            severity += a*b+1
            # print(a)
            

print(f'Answer 2 is {t_delay}')