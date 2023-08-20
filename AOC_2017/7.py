# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 20:42:28 2023

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

import bigtree

# [fname] = ["7_test.txt"]
[fname] = ["7.txt"]

# with open(fname, 'r') as file:
#     prog = file.read().splitlines()
    
df = pd.read_csv(fname, sep=" -> ", header=None, names = ["parent", "children"], engine='python')


df[["parent", "weight"]] = df["parent"].str.split(" ", expand=True)
df["weight"] = df["weight"].str.strip('(').str.strip(')').astype(int)

# weigth = dict(zip(df.parent, df.weight))

df["children"] = df["children"].str.split(', ')

df = df.set_index('parent')

def find_parent(child, df):
    parent = None
    for i in range(len(df)):
        if df.iloc[i, 0] is not None:
            if child in df.iloc[i, 0]:
                parent = df.iloc[i].name
    
    if parent is None:
        return child
    else:
        return find_parent(parent, df)

parent = find_parent(df.iloc[0].name, df)

print(f'Answer 1 is {parent}')


class Tree:
    def __init__(self, name, weight, child_list, df):
        self.name = name
        self.weight = weight
        self.child_list = child_list
        self.children = []
        self.towers = []
        self.total_weight = weight
        
        if child_list is not None:
            for child in child_list:
                self.children.append(Tree(child, df.loc[child, 'weight'], df.loc[child, 'children'], df))
                self.total_weight += self.children[-1].total_weight
                self.towers.append(self.children[-1].total_weight)

tree = Tree(parent, df.loc[parent, 'weight'], df.loc[parent, 'children'], df)

Q = [tree]

diff = 0

while Q or diff == 0:
    this_tree = Q.pop()
    towers = this_tree.towers
    if len(set(towers)) == 1:
        Q = Q + this_tree.children
    else:
        if towers[1] == towers[2]:
            odd = 0
        elif towers[0] == towers[2]:
            odd = 1
        else:
            odd = 2
        
        delta = towers[(odd+1)%3] - towers[odd]
        child = this_tree.child_list[odd]
        diff = df.loc[child, 'weight'] + delta
    
    

print(f'Answer 2 is {diff}')