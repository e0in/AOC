# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:51:13 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def dragon(a):
    b = a
    b = b.replace('1', 't').replace('0', '1').replace('t', '0')
    
    return a + '0' + b[::-1]

assert dragon('1') == '100'
assert dragon('0') == '001'
assert dragon('11111') == '11111000000'
assert dragon('111100001010') == '1111000010100101011110000'

def checksum(s):
    ret = []
    
    for i in range(0, len(s), 2):
        if s[i:i+2] in ['00', '11']:
            ret.append('1')
        else:
            ret.append('0')
    
    ret = "".join(ret)
    if not bool(len(ret)%2):
        return checksum(ret)
    else:
        return ret

assert checksum('110010110100') == '100'

def disc_fill(l, s):
    
    while(len(s)) < l:
        s = dragon(s)
    
    s = s[:l]
    
    return checksum(s)

assert disc_fill(20, '10000') == '01100'


print(f"Answer 1 is {disc_fill(272, '01110110101001000')}")



print(f"Answer 2 is {disc_fill(35651584, '01110110101001000')}")
