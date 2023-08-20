# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:58:15 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def adaptor(fname):
    #df = pd.read_csv(fname, header=None, engine='python')
    jolts = np.loadtxt(fname, dtype = "int")
    jolts = np.append(jolts, 0)
    
    jolts.sort()
    
    d = np.diff(jolts)
    d = np.append(d, 3)
    
    bins = np.bincount(d).tolist()
    #print(bins)
    
    return(bins)

assert adaptor("10_test2.txt") == [0, 22, 0, 10]

ans1 = adaptor("10.txt")

print(f"Answer 1 is {ans1[1]*ans1[3]}")



def vec_translate(a, my_dict):
    a = np.array(a)
    return np.vectorize(my_dict.__getitem__)(a)

n_dict = {1:1, 2:2, 3:4, 4:7, 5:12}


fname = "10.txt"

#df = pd.read_csv(fname, header=None, engine='python')
jolts = np.loadtxt(fname, dtype = "int")
jolts = np.append(jolts, 0)

jolts.sort()

d = np.diff(jolts)
d = np.append(d, 3)

d = d == 1

l = np.diff(np.where(np.concatenate(([d[0]], d[:-1] != d[1:],[True])))[0])[::2]

print(l)

print(vec_translate(l, n_dict).prod())


# #reddit
# from itertools import groupby
# import operator

# def parse_input(raw):
#     return sorted(int(n) for n in raw.splitlines())

# with open('10.txt') as file:
#     input10 = parse_input(file.read())

# def get_differences(joltages):
#     return list(map(
#         operator.sub,
#         joltages + [joltages[-1] + 3],
#         [0] + joltages
#     ))

# def multiply_diffs(differences):
#     return differences.count(1) * differences.count(3)

# def count_arrangements(differences):
#     return math.prod(
#         (2 ** (len(m) - 1)) - (len(m) == 4)        
#         for k, g in groupby(differences)
#         if k == 1 and len((m := list(g))) > 1
#     )

# differences = get_differences(input10)
# answer1 = multiply_diffs(differences)
# answer2 = count_arrangements(differences)