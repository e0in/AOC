# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 14:48:12 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd

total = 0

with open('12.txt', 'r') as file:
    input12 = file.read()

Q = [eval(input12)]

while Q:
    list_in = Q.pop()
    if isinstance(list_in, dict):
        for elem in list_in:
            if isinstance(list_in[elem], str):
                pass
            elif isinstance(list_in[elem], int):
                total += list_in[elem]
            else:
                Q.append(list_in[elem])
    else:
        for elem in list_in:
            if isinstance(elem, str):
                pass
            elif isinstance(elem, int):
                total += elem
            else:
                Q.append(elem)

print(f'Answer 1 is {total}')
    
    
total2 = 0

Q = [eval(input12)]

while Q:
    list_in = Q.pop()
    if isinstance(list_in, dict):
        if any([val=='red' for val in list_in.values()]):
            pass
        else:
            for elem in list_in:
                if isinstance(list_in[elem], str):
                    pass
                elif isinstance(list_in[elem], int):
                    total2 += list_in[elem]
                else:
                    Q.append(list_in[elem])
    else:
        for elem in list_in:
            if isinstance(elem, str):
                pass
            elif isinstance(elem, int):
                total2 += elem
            else:
                Q.append(elem)



print(f'Answer 2 is {total2}')