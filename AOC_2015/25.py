# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:21:50 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = 3029; y = 2947

def code_box(x, y):
    
    rowhead = x + (y-1)
    Tn = round(rowhead * (rowhead + 1) / 2)
    n = Tn - (rowhead - x)
    
    i = 1
    code = 20151125
    
    while i < n:
        i += 1
        code *= 252533
        code = code%33554393

    return code


print(f'Answer 1 is {code_box(x, y)}')

