# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:55:51 2022

@author: ehorgan
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Selector, put True for test data
# [fname] = ["22_test.txt"]
[fname] = ["22.txt"]

with open(fname, 'r') as file:
    mnk_map = file.read().splitlines()# x.replace(': ', '=') for x in 

direc = mnk_map[-1]
direc = direc.replace('R', ',R,').replace('L', ',L,').split(',')


mnk_map = mnk_map[:-2]

max_l = max([len(x) for x in mnk_map])
mnk_map = [list(f'{x:{" "}{"<"}{max_l}}') for x in mnk_map]

trail = np.array(mnk_map)
x_init = np.where((trail[0, :] != ' ') & (trail[0, :] != '#'))[0][0]+1
x = np.where((trail[0, :] != ' ') & (trail[0, :] != '#'))[0][0]+1
trail = np.pad(trail, pad_width = 1, constant_values = ' ')

y = 1
facing = 0

facing_dict = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)} # y, x

for val in direc:
    # print(val, y, x, facing)
    if val == 'R':
        facing = (facing + 1)%4
    elif val == 'L':
        facing = (facing - 1)%4
    else:
        val = int(val)
        dx = facing_dict[facing]
        
        # can_move = True
        
        # while can_move:
        for i in range(val):
            [y_new, x_new] = [y + dx[0], x + dx[1]]
            if trail[y_new, x_new] == '#':
                break
                # can_move = False
            elif trail[y_new, x_new] == '.':
                [y, x] = [y_new, x_new]
            else:
                if facing in [0, 2]: # x-movement
                    valid_sites = np.where((trail[y, :] != ' '))[0]
                    if facing == 0:
                        [y_new, x_new] = [y, valid_sites[0]]
                    else:
                        [y_new, x_new] = [y, valid_sites[-1]]
                else: # y-movement
                    valid_sites = np.where((trail[:, x] != ' '))[0]
                    if facing == 1:
                        [y_new, x_new] = [valid_sites[0], x]
                    else:
                        [y_new, x_new] = [valid_sites[-1], x]
                
                if trail[y_new, x_new] == '#':
                    break
                    # can_move = False
                else:
                    [y, x] = [y_new, x_new]
    # print(y, x, facing)

print(f'Answer 1 is {(1000 * (y)) + (4* (x)) + facing}')

x = x_init
y = 1
facing = 0

face_area = int((trail != ' ').sum()/6)
face_len  = int(math.sqrt(face_area))

def curr_face(y, x):
    if x > 100:
        return 1
    elif y > 150:
        return 6
    elif x < 51:
        return 5
    elif y > 100:
        return 4
    elif y > 50:
        return 3
    else:
        return 2

def face_shift(y, x, facing):
    face_num = curr_face(y, x)
    
    if face_num == 1:
        if facing == 1:
            return [x-50, 100, 2]
        elif facing == 0:
            return [151-y, 100, 2]
        else: # facing == 3
            return [200, x-100, 3]
    elif face_num == 2:
        if facing == 3:
            return [100+x, 1, 0]
        else: # facing == 2
            return [100+y, 1, 0]
    elif face_num == 3:
        if facing == 0:
            return [50, 50+y, 3]
        else: # facing == 2
            return [101, y-50, 1]
    elif face_num == 4:
        if facing == 0:
            return [151-y, 150, 2]
        else: # facing == 1
            return [100+x, 50, 2]
    elif face_num == 5:
        if facing == 3:
            return [50+x, 51, 0]
        else: # facing == 2
            return [151-y, 51, 0]
    elif face_num == 6:
        if facing == 0:
            return [150, y-100, 3]
        elif facing == 1:
            return [1, x+100, 1]
        else: # facing == 2
            return [1, y-100, 1]

for val in direc:
    # print(val, y, x, facing)
    if val == 'R':
        facing = (facing + 1)%4
    elif val == 'L':
        facing = (facing - 1)%4
    else:
        val = int(val)
        dx = facing_dict[facing]
        
        # can_move = True
        
        # while can_move:
        for i in range(val):
            [y_new, x_new] = [y + dx[0], x + dx[1]]
            if trail[y_new, x_new] == '#':
                break
                # can_move = False
            elif trail[y_new, x_new] == '.':
                [y, x] = [y_new, x_new]
            else:
                [y_new, x_new, f_new] = face_shift(y, x, facing)
                if trail[y_new, x_new] == '#':
                    break
                    # can_move = False
                else:
                    [y, x, facing] = [y_new, x_new, f_new]
    # print(y, x, facing)

print(f'Answer 2 is {(1000 * (y)) + (4* (x)) + facing}')
