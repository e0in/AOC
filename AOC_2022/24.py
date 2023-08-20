# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 11:04:07 2022

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

import heapq
from collections import defaultdict

# fname = '24_test.txt'
fname = '24.txt'

with open(fname, 'r') as file:
    ice_map = file.read().splitlines()

# ice_arr = np.array([list(x) for x in ice_map])

l = len(ice_map) - 2
w = len(ice_map[0]) - 2

init_pos = 1+0j
fin_pos = w + (l+1) * 1j
space = set()
ice = []
# for y in range(1, l+1):
#     for x in range(1, w+1):
#         space.add(x + y*1j)
        
for y, line in enumerate(ice_map):
    for x, char in enumerate(line):
        if char != '#':
            space.add(x + y*1j)
            if char == '<':
                ice.append((x + y*1j, -1))
            elif char == '>':
                ice.append((x + y*1j, 1))
            elif char == '^':
                ice.append((x + y*1j, 0-1j))
            elif char == 'v':
                ice.append((x + y*1j, 0+1j))

# space.add(fin_pos)

moves = [0, 1, -1, 0+1j, 0-1j]

def bool_arr(space):
    # yx = [x[0] for x in ice]
    
    x = [int(x.real) for x in space]
    y = [int(y.imag) for y in space]
    
    [ymax, xmax] = [max(y), max(x)]
    A = np.zeros((ymax+1, xmax+1), dtype=bool)
    A[y, x] = True
    return A#[1:, 1:]

# plt.imshow(bool_arr(space))

def int_arr(ice):
    # val_dict = {-1:10, 1:100, 0-1j:1000, 0+1j:10000}
    val_dict = {-1:10, 1:11, 0-1j:20, 0+1j:21}
    
    x = [int(x[0].real) for x in ice]
    y = [int(y[0].imag) for y in ice]
    
    [ymax, xmax] = [max(y), max(x)]
    A = np.zeros((ymax+1, xmax+1), dtype=int)
    for elem in ice:
        A[int(elem[0].imag), int(elem[0].real)] += val_dict[elem[1]]
    
    return A[1:, 1:]
# plt.imshow(int_arr(ice))

def ice_move(ice, l, w):
    new_ice = []
    for par in ice:
        cl = par[0]
        direc= par[1]
        if direc == 1 or direc == -1:
            x = (cl.real-1+direc)%w + 1
            y = cl.imag * 1j
        else:
            x = cl.real
            y = ((cl.imag-1+direc.imag)%l + 1) * 1j
        new_ice.append((x+y, direc))
    return new_ice

cache = {0:ice}
cacheset = {0:set([x[0] for x in ice])}

def ice_n(ice, l, w, n):
    if n not in cache:
        cache[n] = ice_move(ice_n(ice, l, w, n-1)[0], l, w)
        cacheset[n] = set([x[0] for x in cache[n]])
    return cache[n], cacheset[n]

# Q = [[0, 0, 0, (0, 1)]]
# D = np.full([l+2, w+2], 2**31, dtype='uint')
# i = 0

# while Q:
#     i += 1
#     (_, _, cur_time, yx) = heapq.heappop(Q)
    
#     if cur_time < D[yx[0], yx[1]]:
#         D[yx[0], yx[1]] = cur_time
    
#     if cur_time < D[yx[0], yx[1]] + 20:
    
#         to_end = abs(fin_pos.imag - yx[0]) + abs(fin_pos.real - yx[1])
#         time_diff = D[int(fin_pos.imag), int(fin_pos.real)] - cur_time
        
#         if to_end < time_diff:
#             ice_loc = ice_n(ice, l, w, cur_time+1)[1]
#             new_moves = [(int(yx[0] + n.imag), int(yx[1] + n.real)) for n in moves if yx[0] + n.imag + (yx[1] + n.real)*1j in space.difference(ice_loc)]
#             for m in new_moves:
#                 # Q.append([cur_time+1, m])
#                 heapq.heappush(Q, [to_end, i, cur_time+1, m])


def solve(init_pos, fin_pos, ice, l, w, init_time=0):
    
    Q = [[0, init_time, init_pos]]
    D = np.full([l+2, w+2], 500+init_time, dtype='uint')
    d = defaultdict(lambda:[])

    while Q:
        (_, cur_time, pos) = Q.pop(0)
        yx = [int(pos.imag), int(pos.real)]
        
        if cur_time not in d[pos]:
            d[pos].append(cur_time)
            if cur_time < D[yx[0], yx[1]]:
                D[yx[0], yx[1]] = cur_time
            
            if cur_time < D[yx[0], yx[1]] + 20:
            
                de = fin_pos - pos
                to_end = int(abs(de.imag) + abs(de.real))
                time_diff = D[int(fin_pos.imag), int(fin_pos.real)] - cur_time
                
                if to_end < time_diff:
                    ice_loc = ice_n(ice, l, w, cur_time+1)[1]
                    new_moves = [pos + n for n in moves if (pos + n) in space.difference(ice_loc)]
                    for m in new_moves:
                        Q.append([to_end, cur_time+1, m])
                        Q.sort(key=lambda x:x[0])
    return D[int(fin_pos.imag), int(fin_pos.real)]

ans1 = solve(init_pos, fin_pos, ice, l, w, 0)

print(f'Answer 1 is {ans1}')

trip2 = solve(fin_pos, init_pos, ice, l, w, ans1)
trip3 = solve(init_pos, fin_pos, ice, l, w, trip2)

print(f'Answer 2 is {trip3}')