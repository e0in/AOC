# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 10:23:06 2022

@author: ehorgan
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Selector, put True for test data
[fname] = ["23_test.txt"]
[fname] = ["23_test_2.txt"]
[fname] = ["23.txt"]

with open(fname, 'r') as file:
    elf_map = file.read().splitlines()

elfs = []
k = 0
for i, line in enumerate(elf_map):
    for j in range(len(line)):
        if line[j] == '#':
            elfs.append([k, (i, j), (i, j)]) # id, (y,x), (prop y,x)
            k += 1
# df = pd.DataFrame(elfs, columns = ['y', 'x'])

direc_dict = {0: (-1, 0), 1:(1, 0), 2:(0, -1), 3:(0, 1)} # 0 == N, 1 == S, 2 == W, 3 == E
adj_dict = {0:[(-1, -1), (-1, 0), (-1, 1)],
            1:[(1, -1), (1, 0), (1, 1)],
            2:[(-1, -1), (0, -1), (1, -1)],
            3:[(-1, 1), (0, 1), (1, 1)]} # 0 == N, 1 == S, 2 == W, 3 == E

def adjlots(yx):
    ret = []
    for dy in [-1, 0, 1]:
        for dx in  [-1, 0, 1]:
            ret.append((yx[0]+dy, yx[1]+dx))
    ret.remove(yx)
    return ret

def bool_arr(elfs):
    yx = [x[1] for x in elfs]
    
    loc = tuple(zip(*yx))
    [ymin, xmin] = [min(loc[0]), min(loc[1])]
    if ymin < 0 and ymin < 0:
        yx = [(c[0]-ymin, c[1]-xmin) for c in yx]
    elif ymin < 0 and ymin < 0:
        yx = [(c[0]-ymin, c[1]) for c in yx]
    elif xmin < 0:
        yx = [(c[0], c[1]-xmin) for c in yx]
    
    if ymin < 0 or ymin < 0:
        loc = tuple(zip(*yx))
    
    [ymax, xmax] = [max(loc[0]), max(loc[1])]
    A = np.zeros((ymax+1, xmax+1),dtype=bool)
    A[loc] = True
    return A
# plt.imshow(bool_arr(elfs))

def advance(elfs, n = 1):
    direc = 0
    for _ in range(n):
        direc = direc%4
        conf_sites = set()
        prop_sites = set()
        cur_sites = set([x[1] for x in elfs])
        for elf in elfs:
            adj = set(adjlots(elf[1]))
            if adj.intersection(cur_sites):
                for i in range(4):
                    cdir = (direc + i)%4
                    chk = adj_dict[cdir]
                    chkset = set([(elf[1][0]+x[0], elf[1][1]+x[1]) for x in chk])
                    if not chkset.intersection(cur_sites):
                        new_site = (elf[1][0]+direc_dict[cdir][0], elf[1][1]+direc_dict[cdir][1])
                        if new_site not in prop_sites:
                            elf[2] = new_site
                            prop_sites.add(new_site)
                        else:
                            elf[2] = new_site
                            conf_sites.add(new_site)
                        break
        
        for elf in elfs:
            if elf[2] not in conf_sites:
                elf[1] = elf[2]
        direc += 1
        
    return elfs

# elfs_adv = n_rounds(elfs, 2, 0)
elfs_adv = advance(elfs, n = 1)
elfs10 = bool_arr(elfs_adv)
plt.imshow(elfs10)

ans1 = (elfs10.shape[0] * elfs10.shape[1]) - elfs10.sum()

print(f'Answer 1 is {ans1}')

# direc = 0
# elfs5 = n_rounds(elfs, 5, 0)
# elfs10 = n_rounds(elfs, 10, 0)
# plt.imshow(bool_arr(n_rounds(elfs, 10, 0)))
# elfs1 = advance(elfs, 0)
# plt.imshow(bool_arr(elfs1))
