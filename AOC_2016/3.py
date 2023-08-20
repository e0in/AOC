# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:25:03 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import pytest

tria = np.loadtxt("3.txt", dtype = "int")
test1 = np.array([5, 10, 25]).reshape([1, 3])

def valid_triangle(arr):
    two_sides = arr.sum(axis=1) - arr.max(axis=1)
    valid = two_sides > arr.max(axis=1)
    return sum(valid)

assert valid_triangle(test1) == 0

print(f'Answer 1 is {valid_triangle(tria)}')


test2 = np.loadtxt("3_test2.txt", dtype = "int")

def valid_vert(arr):
    n = len(arr)
    assert n%3 == 0
    
    arr = arr.reshape(n*3, 1, order='F').reshape(n, 3, order='C')
    
    return valid_triangle(arr)

print(f'Answer 2 is {valid_vert(tria)}')