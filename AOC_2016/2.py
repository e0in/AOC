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

test1 = ["ULL", "RRDDD", "LURDL", "UUUUD"]

with open('2.txt', 'r') as file:
    bath = file.read().splitlines()

keypad = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]) # keypad[y][x]

def bath_code(bath):
    code = []
    [x, y] = [1, 1]
    
    for i in bath:
        for j in i:
            if j == "U":
                y = max(0, y-1)
            elif j == "D":
                y = min(2, y+1)
            elif j ==  "L":
                x = max(0, x-1)
            else:
                x = min(2, x+1)
            #print(keypad[y][x])
        
        code.append(keypad[y][x])
        #print("button press")
    
    return "".join(code)
    
assert bath_code(test1) == "1985"

print(f'Answer 1 is {bath_code(bath)}')

diagpad = {
  (2, 0): "1",
  (1, -1): "2", (1, 0): "3", (1, 1): "4",
  (0, -2): "5", (0, -1): "6", (0, 0): "7", (0, 1): "8", (0, 2): "9",
  (-1, -1): "A", (-1, 0): "B", (-1, 1): "C",
  (-2, 0): "D"
}

def diag_code(bath):
    code = []
    [y, x] = [0, -2]
    
    for i in bath:
        for j in i:
            [new_y, new_x] = [y, x]
            if j == "U":
                new_y = y+1
            elif j == "D":
                new_y = y-1
            elif j ==  "L":
                new_x = x-1
            else:
                new_x = x+1
            
            if (new_y, new_x) in diagpad.keys():
                [y, x] = [new_y, new_x]
            #print(diagpad[(y, x)])
        
        code.append(diagpad[(y, x)])
        #print("button press")
    
    return "".join(code)

assert diag_code(test1) == "5DB3"

print(f'Answer 2 is {diag_code(bath)}')