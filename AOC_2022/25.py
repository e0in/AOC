# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 10:39:06 2022

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

fname = '25_test.txt'
fname = '25.txt'

with open(fname, 'r') as file:
    fuel = file.read().splitlines()
    
s_dict = {'2':2, '1':1, '0':0, '-':-1, '=':-2}
decimals = dict(map(reversed, s_dict.items()))
    
def SNAFU_to_DEC(s):
    tot = 0
    for i, chr in enumerate(list(s)[::-1]):
        tot += (5**i) * s_dict[chr]
    return tot

def DEC_to_SNAFU(number):
    value = []

    while number > 0:
        remainder = number % 5
        if remainder > 2:
            number += remainder
            value.append(decimals[remainder - 5])
        else:
            value.append(str(remainder))

        number //= 5

    return ''.join(reversed(value))

tot_fuel = 0

for balloon in fuel:
    tot_fuel += SNAFU_to_DEC(balloon)


print(f'Answer 1 is {DEC_to_SNAFU(tot_fuel)}')

# print(f'Answer 2 is {trip3}')
