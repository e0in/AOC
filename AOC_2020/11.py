# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:40:43 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from copy import deepcopy

test = pd.read_csv("11_test.txt", sep = '', header=None, engine='python')
inputdat = pd.read_csv("11.txt", sep = '', header=None, engine='python')

# Selector, put True for test data
if True:
    seats = test
else:
    seats = inputdat

[l, w] = seats.shape
w -= 2
seats.drop(columns=[0,w+1], inplace=True)
seats.columns = list(range(w))
seats = seats == 'L'


seats_arr = np.array(seats)
seats_arr = np.pad(seats_arr, 1, constant_values=False)
seats_pad = pd.DataFrame(seats_arr)
seats_pad.columns = list(range(-1,w+1))
seats_pad.index = list(range(-1,l+1))

curr = seats_pad.apply(deepcopy)
curr[:][:] = False
#seats = df_pad.copy()

def advance(prev, seats):
    curr = prev.apply(deepcopy)
    
    for i in range(w):
        for j in range(l):
            if seats.loc[j, i]:
                if prev.loc[j, i]:# seat occupied
                    if prev.loc[j-1:j+1, i-1:i+1].sum().sum() >= 5:
                        curr.loc[j, i] = False
                else: # Seat unoccupied
                    if prev.loc[j-1:j+1, i-1:i+1].sum().sum() == 0:
                        curr.loc[j, i] = True
    
    return curr

def stable_state(prev, seats):
    i = 0
    stable = False
    
    while not stable:
        new = advance(prev, seats)
        i += 1
        print(f"i = {i}, n = {new.sum().sum()}")
        # plt.imshow(new)
        # if i%10 == 0:
        #     plt.imshow(new)
        if (new == prev).all().all():
            return new.sum().sum()
        else:
            prev = new

# print(f'Answer 1 is {stable_state(curr, seats)}')

curr = seats_arr.copy()
# prev = curr.copy()
curr[:,:] = False

def sight_advance(prev, seats_arr):
    curr = prev.copy()
    
    for i in range(1, w+1):
        for j in range(1, l+1):
            if seats_arr[j, i]:
                o = 0 # Number of visible seats
                
                o += prev[j-1:0:-1, i].any() #up
                o += prev[j+1:l+1, i].any()    #down
                o += prev[j, i-1:0:-1].any() #left
                o += prev[j, i+1:w+1].any()    #right
                
                tl = min(i, j)
                tr = min(w-i, j)
                dl = min(i, l-j)
                dr = min(w-i, l-j)
                
                o += prev[range(j-1,j-tl-1,-1), range(i-1,i-tl-1,-1)].any() # top left
                o += prev[range(j+1,j+dr+1), range(i+1,i+dr+1)].any()       # down right
                o += prev[range(j-1,j-tr-1,-1), range(i+1,i+tr+1)].any()  # top right
                o += prev[range(j+1,j+dl+1), range(i-1,i-dl-1,-1)].any()     # down left

                if prev[j, i]:# seat occupied
                    if o >= 5:
                        curr[j, i] = False
                else: # Seat unoccupied
                    if o == 0:
                        curr[j, i] = True
    
    return curr

def stable_state2(prev, seats_arr):
    i = 0
    stable = False
    
    while not stable:
        new = sight_advance(prev, seats_arr)
        i += 1
        print(f"i = {i}, n = {new.sum().sum()}")
        # plt.imshow(new)
        # if i%10 == 0:
        #     plt.imshow(new)
        if (new == prev).all().all():
            return new.sum().sum()
        else:
            prev = new

print(f'Answer 2 is {stable_state2(curr, seats_arr)}')

gen1 = sight_advance(curr, seats_arr)
gen2 = sight_advance(gen1, seats_arr)
gen3 = sight_advance(gen2, seats_arr)
prev = gen2



#reddit

from collections import defaultdict


def solve(seats, neighbors, limit):
    while True:
        new_seats = {}
        for seat, occupied in seats.items():
            count = (seats[neighbor] for neighbor in neighbors[seat])
            new_seats[seat] = sum(count) < limit if occupied else not any(count)

        if seats == new_seats:
            return sum(new_seats.values())

        seats = new_seats

with open("11.txt", 'r') as file:
    lines = file.read().splitlines()
#lines = open(0).read().splitlines()
size = len(lines)  # grid width and height are the same
# fmt: off
seats = {
    row + col*1j: False
    for row, line in enumerate(lines)
    for col, char in enumerate(line)
    if char == "L"
}

directions = {
    direction
    for row in (-1, 0, 1)
    for col in (-1, 0, 1)
    if (direction := row + col*1j)  # skip 0+0*j
}

# Precompute all possible (in)direct neighbors of each seat

neighbors_direct = {
    seat: [
        neighbor
        for direction in directions
        if (neighbor := seat + direction) in seats
    ]
    for seat in seats
}
# fmt: on
neighbors_adjacent = defaultdict(list)
for seat in seats:
    for direction in directions:
        neighbor = seat + direction
        while 0 <= neighbor.real < size and 0 <= neighbor.imag < size:
            if neighbor in seats:
                neighbors_adjacent[seat].append(neighbor)
                break
            neighbor += direction

print(solve(seats, neighbors_direct, 4))
print(solve(seats, neighbors_adjacent, 5))