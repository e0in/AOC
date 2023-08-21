# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:31:45 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Selector, put True for test data
if False:
    fname = "13_test.txt"
else:
    fname = "13.txt"

with open(fname, 'r') as file:
    msg = file.read().splitlines()

n = (len(msg)+1)//3

def check_order(lm, rm):
    if isinstance(lm, int) and isinstance(rm, int):
        if lm < rm:
            return [True, True] # Is ordered
        elif lm > rm:
            return [True, False] # is disordered
        else:
            return [False, False]
    elif isinstance(lm, list) and isinstance(rm, list):
        [ll, rl] = [len(lm), len(rm)]
        
        for j in range(min(ll, rl)):
            ret = check_order(lm[j], rm[j])
            if ret[0]:
                return ret
            
        if ll < rl:
            return [True, True] # Is ordered
        elif ll > rl:
            return [True, False] # is disordered
        else:
            return [False, False]
    else:
        if isinstance(lm, int):
            return check_order([lm], rm)
        else:
            return check_order(lm, [rm])


correct_order = []

for i in range(n):
    ls = msg[3*i]
    rs = msg[3*i+1]
    lm = eval(ls)
    rm = eval(rs)
    chk = check_order(lm, rm)
    if chk[1]:
        correct_order.append(i+1)
    
print(f'Answer 1 is {sum(correct_order)}')   

msg = list(filter(None, msg)) + ['[[2]]', '[[6]]']

ordered_msg = [msg.pop()]

new_str = msg.pop()
chk = check_order(eval(ordered_msg[0]), eval(new_str))
if chk[1]:
    ordered_msg.append(new_str)
else:
    ordered_msg.insert(0, new_str)

while msg:
    new_str = msg.pop()
    
    chk = check_order(eval(ordered_msg[-1]), eval(new_str))
    if chk[1]:
        ordered_msg.append(new_str)
    else:
        chk = check_order(eval(new_str), eval(ordered_msg[0]))
        if chk[1]:
            ordered_msg.insert(0, new_str)
        else:
            for j in range(1, len(ordered_msg)):
                chk1 = check_order(eval(ordered_msg[j-1]), eval(new_str))
                chk2 = check_order(eval(new_str), eval(ordered_msg[j]))
                if chk1[1] and chk2[1]:
                    ordered_msg.insert(j, new_str)
    
i1 = ordered_msg.index('[[2]]') + 1
i2 = ordered_msg.index('[[6]]') + 1

print(f'Answer 2 is {i1*i2}')   