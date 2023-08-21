# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:46:02 2022

@author: ehorgan
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import collections

# Selector, put True for test data
# [fname] = ["20_test.txt"]
[fname] = ["20.txt"]

with open(fname, 'r') as file:
    seq = file.read().splitlines()

orig_seq = [(i, int(x)) for i, x in enumerate(seq)]
zero = [a for a in orig_seq if a[1] == 0][0]

n = len(seq)

def mix(order_seq, orig_seq, zero):
    d = collections.deque(orig_seq)
    n = len(seq)
    for i in range(n):
        orig = order_seq[i]
        ind_curr = d.index(orig)
        d.rotate(-ind_curr)
        _, ind_new = d.popleft()
        d.rotate(-ind_new)
        d.appendleft(orig)
    
    ind_zero = d.index(zero)
    d.rotate(-ind_zero)
    new_seq = list(d)    
    return new_seq

new_seq = mix(orig_seq, orig_seq, zero)

print(f'Answer 1 is {new_seq[1000%n][1] + new_seq[2000%n][1] + new_seq[3000%n][1]}')

key = 811589153
key_seq = [(x[0], x[1]*key) for x in orig_seq]
key_order = key_seq.copy()

for i in range(10):
    key_seq = mix(key_order, key_seq, zero)
    # print([x[1] for x in key_seq])

print(f'Answer 2 is {key_seq[1000%n][1] + key_seq[2000%n][1] + key_seq[3000%n][1]}')

