# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 23:00:48 2021

@author: Eoin
"""

import math
import numpy as np
import pandas as pd

test = np.loadtxt("8_test.txt", dtype = "str")
input8 = np.loadtxt("8.txt", dtype = "str")


str_code_char = sum([len(a) for a in input8])

str_code_mem  = sum([len(eval(a)) for a in input8])

print(f'Answer 1 is {str_code_char - str_code_mem}')

str_code_encode  = sum([2 + a.count('\\') + a.count('"') for a in input8])

print(f'Answer 2 is {str_code_encode}')
