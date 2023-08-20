# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:51:40 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# [fname] = ["8_test.txt"]
[fname] = ["9.txt"]

with open(fname, 'r') as file:
    s = file.read()

def traverser(s):
    s = list(s)

    score = 0
    cur_val = 0
    is_garbage = False
    garbage = 0
    
    while s:
        ch = s.pop(0)
        if is_garbage:
            if ch == '!':
                s.pop(0)
            elif ch == '>':
                is_garbage = False
            else:
                garbage += 1
        else:
            if ch == '{':
                cur_val += 1
            elif ch == '}':
                score += cur_val
                cur_val -= 1
            elif ch == '<':
                is_garbage = True
                
    return score, garbage
 

assert traverser("{{{},{},{{}}}}")[0] == 16
assert traverser("{<a>,<a>,<a>,<a>}")[0] == 1
assert traverser("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9
assert traverser("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0] == 9
assert traverser("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3

print(f'Answer 1 is {traverser(s)[0]}')
 
assert traverser("<>")[1] == 0
assert traverser("{<random characters>}")[1] == 17
assert traverser("<<<<>")[1] == 3
assert traverser("<{!>}>")[1] == 2
assert traverser("<!!>")[1] == 0
assert traverser("<!!!>>")[1] == 0
assert traverser('<{o"i!a,<{i<a>')[1] == 10

print(f'Answer 2 is {traverser(s)[1]}')