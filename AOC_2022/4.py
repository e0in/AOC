# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:08:41 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

test = pd.read_csv("4_test.txt", sep=",", header=None, names = ["e1", "e2"], engine='python')
real = pd.read_csv("4.txt", sep=",", header=None, names = ["e1", "e2"], engine='python')

# df = test
df = real

#sp = df["e1"].apply(lambda x: pd.Series(list(x)))

df[["1l", "1h"]] = df["e1"].str.split("-", expand=True).astype('int')
df[["2l", "2h"]] = df["e2"].str.split("-", expand=True).astype('int')

df["1cont"] = (df["2l"] <= df["1l"]) & (df["1h"] <= df["2h"])
df["2cont"] = (df["1l"] <= df["2l"]) & (df["2h"] <= df["1h"])
df["eq"] = (df["1l"] == df["2l"]) & (df["2h"] == df["1h"])

print(f"Answer 1 is {df[['1cont', '2cont']].sum().sum() - df['eq'].sum()}")

df["over"] = ((df["1h"] >= df["2l"]) & (df["1l"] <= df["2h"])) | ((df["2h"] >= df["1l"]) & (df["2l"] <= df["1h"]))

print(f"Answer 2 is {df['over'].sum()}")
