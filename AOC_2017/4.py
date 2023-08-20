# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:15:10 2023

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

with open('4.txt', 'r') as file:
    phrases = file.read().splitlines()

count1 = 0
count2 = 0

for phrase in phrases:
    words = phrase.split()
    if len(words) == len(set(words)):
        count1 += 1
        if len(words) == len(set([frozenset(x) for x in words])):
            count2 += 1

print(f'Answer 1 is {count1}')
print(f'Answer 2 is {count2}')