# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:34:29 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd


test = pd.read_csv("2_test.txt", sep="x", header=None, names = ["l", "w", "h"])
input2 = pd.read_csv("2.txt", sep="x", header=None, names = ["l", "w", "h"])

test.loc[:, "lxw"] = test.loc[:, "l"] * test.loc[:, "w"]
test.loc[:, "lxh"] = test.loc[:, "l"] * test.loc[:, "h"]
test.loc[:, "wxh"] = test.loc[:, "w"] * test.loc[:, "h"]
test.loc[:, "s"] = test.iloc[:,3:6].min(axis = 1)
test.loc[:, "wrap"] = test.iloc[:,3:6].sum(axis = 1)*2 + test.loc[:, "s"]

input2.loc[:, "lxw"] = input2.loc[:, "l"] * input2.loc[:, "w"]
input2.loc[:, "lxh"] = input2.loc[:, "l"] * input2.loc[:, "h"]
input2.loc[:, "wxh"] = input2.loc[:, "w"] * input2.loc[:, "h"]
input2.loc[:, "s"] = input2.iloc[:,3:6].min(axis = 1)
input2.loc[:, "wrap"] = input2.iloc[:,3:6].sum(axis = 1)*2 + input2.loc[:, "s"]

print(f'Answer 1 is {input2.loc[:, "wrap"].sum()}')

# %% Part 2

test.loc[:, "V"] = test.loc[:, "l"] * test.loc[:, "w"] * test.loc[:, "h"]
test.loc[:, "per"] = 2 * (test.iloc[:,0:3].sum(axis=1) - test.iloc[:,0:3].max(axis=1))
test.loc[:, "ribbon"] = test.loc[:, "V"] + test.loc[:, "per"]


input2.loc[:, "V"] = input2.loc[:, "l"] * input2.loc[:, "w"] * input2.loc[:, "h"]
input2.loc[:, "per"] = 2 * (input2.iloc[:,0:3].sum(axis=1) - input2.iloc[:,0:3].max(axis=1))
input2.loc[:, "ribbon"] = input2.loc[:, "V"] + input2.loc[:, "per"]

print(f'Answer 2 is {input2.loc[:, "ribbon"].sum()}')