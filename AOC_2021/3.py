# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:34:29 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

#test = np.genfromtxt("2_test.txt")
#input2 = np.genfromtxt("2_1.txt")

test = pd.read_csv("3_test.txt", sep=" ", header=None, dtype="str")
input3 = pd.read_csv("3.txt", sep=" ", header=None, dtype="str")

test = test[0].apply(lambda x: pd.Series(list(x))).astype("int")
input3 = input3[0].apply(lambda x: pd.Series(list(x))).astype("int")

gamma_array_t = (1*(test.sum() > 6)).astype("str").str.cat()
epsilon_array_t = (1*(test.sum() < 6)).astype("str").str.cat()

gamma_t = int(gamma_array_t, 2)
epsilon_t = int(epsilon_array_t, 2)

gamma_array = (1*(input3.sum() > (len(input3)/2))).astype("str").str.cat()
epsilon_array = (1*(input3.sum() < (len(input3)/2))).astype("str").str.cat()

gamma = int(gamma_array, 2)
epsilon = int(epsilon_array, 2)

print(f'Answer 1 is {gamma * epsilon}')

# %% Part 2

#oxy = test.copy()
#co2 = test.copy()

oxy = input3.copy()
co2 = input3.copy()

for i in range(input3.shape[1]):
    g = int(sum(oxy[i] == 1) >= sum(oxy[i] == 0))
    
    oxy = oxy.loc[oxy[i] == g,:]
    
    if len(oxy) == 1:
        break

for i in range(input3.shape[1]):
    e = int(sum(co2[i] == 1) < sum(co2[i] == 0))
    
    co2 = co2.loc[co2[i] == e,:]
    
    if len(co2) == 1:
        break

oxy_array = oxy.astype("str").squeeze().str.cat()
co2_array = co2.astype("str").squeeze().str.cat()


print(f'Answer 2 is {int(oxy_array, 2) * int(co2_array, 2)}')