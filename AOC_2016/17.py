# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:09:18 2022

@author: Eoin
"""


import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

import hashlib

passcode = 'vkjiggvb'

def path_solve(passcode):
    min_dist = 10000
    min_path = ''
    #     x  y  path steps
    Q = [[0, 0, '', 0]]
    
    while Q:
        [x, y, path, dist] = Q.pop(0)
        
        if 0 <= x <= 3 and 0 <= y <= 3 and dist < min_dist:
            
            if x == y == 3:
                min_path = path
                min_dist = len(path)
            else:
            
                p_hash = passcode + path
                s_str = hashlib.md5(p_hash.encode('utf-8')).hexdigest()[:4]
                
                if s_str[0] in ['b', 'c', 'd', 'e', 'f']:
                    Q.append([x, y-1, path + 'U', dist+1])
                if s_str[1] in ['b', 'c', 'd', 'e', 'f']:
                    Q.append([x, y+1, path + 'D', dist+1])
                if s_str[2] in ['b', 'c', 'd', 'e', 'f']:
                    Q.append([x-1, y, path + 'L', dist+1])
                if s_str[3] in ['b', 'c', 'd', 'e', 'f']:
                    Q.append([x+1, y, path + 'R', dist+1])
    
    return min_path

assert path_solve('ihgpwlah') == 'DDRRRD'
assert path_solve('kglvqrro') == 'DDUDRLRRUDRD'
assert path_solve('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'

print(f"Answer 1 is {path_solve(passcode)}")

def path_max(passcode):
    max_dist = 0
    #     x  y  path steps
    Q = [[0, 0, '', 0]]
    
    while Q:
        [x, y, path, dist] = Q.pop(0)
        
        if 0 <= x <= 3 and 0 <= y <= 3:
            
            if x == y == 3:
                if len(path) > max_dist:
                    max_dist = len(path)
            else:
            
                p_hash = passcode + path
                s_str = hashlib.md5(p_hash.encode('utf-8')).hexdigest()[:4]
                
                if s_str[0] in ['b', 'c', 'd', 'e', 'f']:
                    Q.append([x, y-1, path + 'U', dist+1])
                if s_str[1] in ['b', 'c', 'd', 'e', 'f']:
                    Q.append([x, y+1, path + 'D', dist+1])
                if s_str[2] in ['b', 'c', 'd', 'e', 'f']:
                    Q.append([x-1, y, path + 'L', dist+1])
                if s_str[3] in ['b', 'c', 'd', 'e', 'f']:
                    Q.append([x+1, y, path + 'R', dist+1])
    
    return max_dist

assert path_max('ihgpwlah') == 370
assert path_max('kglvqrro') == 492
assert path_max('ulqzkmiv') == 830

print(f"Answer 2 is {path_max(passcode)}")
