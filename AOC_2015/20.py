# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 22:58:45 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sympy import divisors
from scipy.optimize import minimize_scalar

trgt = 29000000

# for i in range(1, 10):
#     presents = sum(divisors(i))*10
#     print(i, presents)

# def house_presents(i):
#     return sum(divisors(round(i)))*10 - trgt

# house_vec = np.vectorize(house_presents)
# # x = np.arange(0, 2*trgt, 1000)
# x = np.arange(0000, 2000000, 1000)
# y = house_vec(x)

# plt.figure()
# plt.plot(x, y)
# #plt.ylim([0, 100000])
# plt.show()

# res = minimize_scalar(house_presents, bounds=(680000, 720000), method='bounded')
# x = round(res.x)
# print(house_presents(x))

# min_house = -1
# house = 600000

while min_house < 0:
    house += 1
    presents = sum(divisors(house)) * 10
    if presents >= trgt:
        min_house = house

print(f'Answer 1 is {min_house}')

min_house = -1
house = 600000

while min_house < 0:
    house += 1
    presents = sum([d for d in divisors(house) if house/d <= 50]) * 11
    if presents >= trgt:
        min_house = house

print(f'Answer 2 is {min_house}')