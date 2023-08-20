# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:25:03 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest


msg = pd.read_csv("6.txt", sep=" ", header=None, engine='python')[0].apply(lambda x: pd.Series(list(x)))
test1 = pd.read_csv("6_test.txt", sep=" ", header=None, engine='python')[0].apply(lambda x: pd.Series(list(x)))

def err_corr(df):
    ans = []
    ans2 = []
    for i in range(df.shape[1]):
        ans.append(df[i].value_counts().index[0])
        ans2.append(df[i].value_counts().index[-1])
    
    return "".join(ans), "".join(ans2)

assert err_corr(test1)[0] == 'easter'
    
print(f'Answer 1 is {err_corr(msg)[0]}')

assert err_corr(test1)[1] == 'advent'

print(f'Answer 2 is {err_corr(msg)[1]}')