# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:34:10 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

from collections import deque
from functools import reduce
from operator import xor

# in_text = 'flqrgnkx' # practice
in_text = 'hwlqcszp'

def knot_logic(sizes, iterations=64):
    circle = deque(range(256))
    skip = 0
    for _ in range(iterations):
        for group_size in sizes:
            knot = [circle.popleft() for _ in range(group_size)]
            circle += reversed(knot)
            circle.rotate(-skip)
            skip += 1
    unwind = iterations * sum(sizes) + skip * (skip-1) // 2
    circle.rotate(unwind)
    return list(circle)

def knothash(word):
    ascii_sizes = [ord(c) for c in word] + [17, 31, 73, 47, 23]
    numbers = knot_logic(ascii_sizes)
    SIZE = 256
    BLOCK_SIZE = 16
    block = lambda i: numbers[i*BLOCK_SIZE : (i+1)*BLOCK_SIZE]
    dense = [reduce(xor, block(i)) for i in range(SIZE // BLOCK_SIZE)]
    return ''.join(f'{n:02x}' for n in dense)


def hex_to_bin(hex_in):
    return bin(int(hex_in, 16))[2:].zfill(128)
    
# dat_count = 0

matrix = np.zeros([128, 128], dtype = bool)

for i in range(128):
    str_in = in_text + '-' + str(i)
    data = hex_to_bin(knothash(str_in))
    # dat_count += data.count('1')
    matrix[i, :] = np.array(list(data))=='1'

print(f'Answer 1 is {matrix.sum()}')

from skimage import measure
all_labels = measure.label(matrix, connectivity=1)

print(f'Answer 1 is {all_labels.max()}')

# def knothash(word):
#     lens = [ord(x) for x in word]
#     lens.extend([17,31,73,47,23])
#     nums = [x for x in range(0,256)]
#     pos = 0
#     skip = 0
#     for _ in range(64):
#         for l in lens:
#             to_reverse = []
#             for x in range(l):
#                 n = (pos + x) % 256
#                 to_reverse.append(nums[n])
#             to_reverse.reverse()
#             for x in range(l):
#                 n = (pos + x) % 256
#                 nums[n] = to_reverse[x]
#             pos += l + skip
#             pos = pos % 256
#             skip += 1
#     dense = []
#     for x in range(0,16):
#         subslice = nums[16*x:16*x+16]
#         dense.append('%02x'%reduce((lambda x,y: x ^ y),subslice))
#     return(''.join(dense))