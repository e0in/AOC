# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:46:46 2023

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

from collections import defaultdict

[fname] = ["25_test.txt"]
[fname] = ["25.txt"]

with open(fname, "r") as file:
    turing = file.read().splitlines()

def tape_dir(string):
    if string == 'left.':
        return -1
    else:
        return 1

state = turing[0][-2]
chk_steps = int(turing[1].split('after ')[1].split()[0])

tape = defaultdict(int)
j = 0

l = len(turing)

state_dict = dict()

for i in range(3, l-8, 10):
    # print(i)
    cur_state = turing[i][-2] # Written val, 
    state_dict[(cur_state, 0)] = [int(turing[i+2][-2]), tape_dir(turing[i+3].split('the ')[1]), turing[i+4][-2]]
    state_dict[(cur_state, 1)] = [int(turing[i+6][-2]), tape_dir(turing[i+7].split('the ')[1]), turing[i+8][-2]]

for k in range(chk_steps):
    [new_val, jump, state] = state_dict[(state, tape[j])]
    tape[j] = new_val
    j += jump
    
print(f'Answer 1 is {sum(tape.values())}')