# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:04:46 2023

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

# [fname] = ["12_test.txt"]
[fname] = ["12.txt"]

with open(fname, "r") as file:
    pipes = file.read().splitlines()
    

import networkx as nx

G = nx.Graph()

programs = set()

for pipe in pipes:
    [origin, targets] = pipe.split(' <-> ')
    programs.add(origin)
    trg = targets.split(', ')
    for dest in trg:
        G.add_edge(origin, dest)
        programs.add(dest)
        
def group_find(origin='0'):

    zero_grp = []
    Q = [origin]
    
    while Q:
        curr = Q.pop()
        if curr not in zero_grp:
            zero_grp.append(curr)
            neighbours = list(G.adj[curr])
            for ng in neighbours:
                if ng not in zero_grp:
                    Q.append(ng)
    return zero_grp

zero_grp = group_find('0')

print(f'Answer 1 is {len(set(zero_grp))}')

programs = list(programs)
programs.sort()

new_programs = [x for x in programs if x not in zero_grp]

grp_cnt = 1

while new_programs:
    origin = new_programs[0]
    new_grp = group_find(origin)
    new_programs = [x for x in new_programs if x not in new_grp]
    grp_cnt += 1
    
print(f'Answer 2 is {grp_cnt}')    

# nx.draw(G, with_labels=True, font_weight='bold')
