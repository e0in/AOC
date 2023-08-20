# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:25:03 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def decomp(s, recurse=False):
    ret = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            j = i+s[i:].find(')')+1
            [nchar, reps] = [int(x) for x in s[i+1:j-1].split('x')]
            i = j + nchar
            ret.append(s[j:j+nchar]*reps)
        else:
            ret.append(s[i])
            i += 1
    
    out_s = "".join(ret)
    
    if recurse:
        if out_s.find('(') >= 0:
            return decomp(out_s, recurse=True)
    
    out_strip = out_s.replace(" ", "")
    out_strip = out_strip.replace('\n', '')
    
    return out_s, len(out_strip)
    
assert decomp('ADVENT')[1] == 6
assert decomp('A(1x5)BC') == ('ABBBBBC', 7)
assert decomp('(3x3)XYZ') == ('XYZXYZXYZ', 9)
assert decomp('A(2x2)BCD(2x2)EFG') == ('ABCBCDEFEFG', 11)
assert decomp('(6x1)(1x3)A') == ('(1x3)A', 6)
assert decomp('X(8x2)(3x3)ABCY') == ('X(3x3)ABC(3x3)ABCY', 18)

with open('9.txt', 'r') as file:
    comp_text = file.read()#.splitlines()
    
print(f'Answer 1 is {decomp(comp_text)[1]}')

assert decomp('X(8x2)(3x3)ABCY', recurse=True) == ('XABCABCABCABCABCABCY', 20)
assert decomp('(27x12)(20x12)(13x14)(7x10)(1x12)A', recurse=True)[1] == 241920
assert decomp('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', recurse=True)[1] == 445

def decomp_length(s):
    s = s.replace(" ", "")
    weight = np.ones(len(s), dtype = 'int64')
    i = 0
    while i < len(s):
        if s[i] == '(':
            j = i+s[i:].find(')')+1
            [nchar, reps] = [int(x) for x in s[i+1:j-1].split('x')]
            #w = weight[i] * reps
            weight[i:j] = 0
            weight[j:j+nchar] = weight[j:j+nchar]*reps
            i = j
        else:
            i += 1
    
    return weight

assert decomp_length('A(1x5)BC').sum() == 7
assert decomp_length('X(8x2)(3x3)ABCY').sum() == 20
assert decomp_length('(27x12)(20x12)(13x14)(7x10)(1x12)A').sum() == 241920
assert decomp_length('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN').sum() == 445

print(f'Answer 2 is {decomp_length(comp_text).sum()}')

