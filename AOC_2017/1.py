# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:25:14 2023

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# Selector, put True for test data
# [fname] = ["1_test.txt"]
[fname] = ["1.txt"]

with open(fname, 'r') as file:
    input1 = file.read().splitlines()

nums = list(input1[0])
nums = [int(x) for x in nums]

arr = np.array(nums)

def match_sum(nums):
    arr = np.array(nums)
    
    diff = np.diff(nums)
    
    mask = diff == 0
    mask = np.append(mask, nums[0] == nums[-1])
    
    count = np.sum(arr[mask])
    
    return count

assert match_sum([1, 1, 2, 2]) == 3

print(f'Answer 1 is {match_sum(nums)}')


def split_sum(arr):    
    [arr1, arr2] = np.split(arr, 2)
    
    mask = arr1 == arr2
    
    count = np.sum(arr1[mask] * 2)
    
    return count

assert split_sum(np.array([1, 2, 1, 2])) == 6



print(f'Answer 2 is {split_sum(arr)}')