# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:34:29 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

import hashlib


test = "pqrstuv"
#hashret = hashlib.md5("pqrstuv1048970".encode('utf-8')).hexdigest()

input3 = "iwrupvqb"

for i in range(1000000):
    hashret = hashlib.md5(f'{input3}{i}'.encode('utf-8')).hexdigest()
    if hashret[0:5] == '00000':
        break
    

print(f'Answer 1 is {i}')

# %% Part 2



for i in range(10000000):
    hashret = hashlib.md5(f'{input3}{i}'.encode('utf-8')).hexdigest()
    if hashret[0:6] == '000000':
        break
    

print(f'Answer 2 is {i}')