# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:36:29 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest


s = np.arange(256)
ls = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]

def rope_hash(s, ls, skip_size = 0, origin_roll = 0):
    if origin_roll != 0:
        s = np.roll(s, origin_roll)

    roll = 0
    # print(s)
    
    for l in ls:
        s[:l] = np.flip(s[:l])
        s = np.roll(s, - l - skip_size)
        roll += - l - skip_size
        skip_size += 1
        # print(s)
    
    s = np.roll(s, -roll-origin_roll)
    # print(s)
    return [s, skip_size, roll+origin_roll]

assert np.all(rope_hash(np.array([0, 1, 2, 3, 4]), [3, 4, 1, 5])[0] == np.array([3, 4, 2, 1, 0]))
# assert traverser("{<a>,<a>,<a>,<a>}")[0] == 1

arr = rope_hash(s, ls)[0]

print(f'Answer 1 is {arr[0]*arr[1]}')

def to_ord(nums):
    chars = [str(x) for x in nums]
    return [ord(x) for x in ','.join(chars)]

def to_ord2(chars):
    return to_ord(chars) + [17, 31, 73, 47, 23]

assert to_ord2([1, 2, 3]) == [49,44,50,44,51,17,31,73,47,23]

def multi_hash(s, ls, n):
    roll = 0
    skip = 0
    for i in range(n):
        [s, skip, roll] = rope_hash(s, ls, skip, roll)
    
    return s

def hex_rep(arr):
    arr = arr.astype(str)
    dense = []
    out_str = []
    
    for i in range(16):
        sub_arr = list(arr[i*16:i*16+16])
        dense.append(eval('^'.join(sub_arr)))
    
    for elem in dense:
        hexa = f'{elem:x}'
        new_str = f'{hexa:>02}'
        out_str.append(new_str)
    
    return(dense, ''.join(out_str))

arr = multi_hash(s, to_ord2([1,2,3]), 64)

[dense, out_str] = hex_rep(arr)



print(f'Answer 2 is {out_str}')




###reddit 


from functools import reduce

lens = [ord(x) for x in open('10.txt','r').read().rstrip()]
lens.extend([17,31,73,47,23])
nums = [x for x in range(0,256)]
pos = 0
skip = 0
for _ in range(64):
    for l in lens:
        to_reverse = []
        for x in range(l):
            n = (pos + x) % 256
            to_reverse.append(nums[n])
        to_reverse.reverse()
        for x in range(l):
            n = (pos + x) % 256
            nums[n] = to_reverse[x]
        pos += l + skip
        pos = pos % 256
        skip += 1
dense = []
for x in range(0,16):
    subslice = nums[16*x:16*x+16]
    dense.append('%02x'%reduce((lambda x,y: x ^ y),subslice))
print(''.join(dense))
