# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:49:56 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

test = 'hijklmmn'
test2 = 'abcdefghijklmnopqrstuvwxyz'
test3 = 'abcdefgh'
test4 = 'ghijklmn'

#in11 = test3
#in11 = test4
in11 = 'cqjxjnds'

#np.base_repr(13, 26)
#ord('a')
#chr(97)

def str_to_int(init_str):
    arr = []
    for char in init_str:
        arr.append(str(np.base_repr(ord(char)-97, 26)))
    
    input_b26 = ''.join(arr)
    
    return(int(input_b26, 26))

def int_to_str(init_int):
    arr = [chr(int(char, 26)+97) for char in np.base_repr(init_int, 26)]
    return(''.join(arr))

def int_to_b26_arr(init_int):
    pass_ls = np.base_repr(init_int, 26)
    return([int(char, 26) for char in pass_ls])

def pass_check(pass_arr):
    if isinstance(pass_arr, str):
        pass_arr = int_to_b26_arr(str_to_int(pass_arr))
    
    n = len(pass_arr)
    check1 = False
    
    for i in range(n-2):
        if (pass_arr[i]+2) == (pass_arr[i+1]+1) == pass_arr[i+2]:
            check1 = True
    if not check1:
        return(False)
    
    if (8 in pass_arr) or (14 in pass_arr) or (11 in pass_arr):
        return(False)
    
    rep = set(np.array(pass_arr[0:-1])[np.diff(pass_arr) == 0])
    if len(rep) < 2:
        return(False)
    else:  
        return(True)


curpass = (str_to_int(in11)) + 1

while not pass_check(int_to_b26_arr(curpass)):
    curpass += 1
    
print(f'Answer 1 is {int_to_str(curpass)}')

curpass += 1

while not pass_check(int_to_b26_arr(curpass)):
    curpass += 1
    
print(f'Answer 2 is {int_to_str(curpass)}')


