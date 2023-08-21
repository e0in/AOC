# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:54:50 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

with open('7.txt', 'r') as file:
    term = file.read().splitlines()
    
filesum = 0
req_pt2 = 10822529
cur_dir = '/'
cur_size = 50822529
    
class tree():
    """Tree data structure"""
    def __init__(self, name):
        self.name = name
        self.files = []
        self.sizes = []
        self.tf_size = 0
        self.subdir = []
        # self.sb_sizes = []
        self.sb_size = 0

    def explore(self, term):
        i = 0
        while i < len(term):
            print([i, term[i], self.name, len(term)])
            if term[i] == "$ ls" or term[i] == "$ cd /" or term[i][:3] == 'dir':
                i += 1
            elif term[i][:7] == "$ cd ..":
                return [i+1, self.tf_size + self.sb_size]
            elif term[i][0] == "$":
                self.subdir.append(tree(term[i][5:]))
                print(i, term[i], self.name)
                [ret, sds] = self.subdir[-1].explore(term[i+1:])
                self.sb_size += sds
                # self.sb_sizes.append(sds)
                
                if sds <= 100000:
                    global filesum
                    filesum += sds
                
                global req_pt2
                global cur_size
                if req_pt2 <= sds < cur_size:
                    global cur_dir
                    cur_dir = term[i][5:]
                    cur_size = sds
                
                i += ret+1
            else:
                [s, n] = term[i].split(' ')
                s = int(s)
                self.files.append(n) 
                self.sizes.append(s)
                self.tf_size = sum(self.sizes)
                i += 1
        
        return [i+1, self.tf_size + self.sb_size]
    
    def smallest_dir(self, req_size):
        cur_dir = '/'
        cur_size = self.tf_size + self.sb_size
        
        return 1
    
    def ret_size(self, req_size, cur_size):
        if req_size <= (self.tf_size + self.sb_size) < cur_size:
            return [self.name, (self.tf_size + self.sb_size)]
            
            
my_tree = tree('/')
my_tree.explore(term)

print(f'Answer 1 is {filesum}')

req_size = 30000000 - 70000000 + (my_tree.tf_size + my_tree.sb_size)

print(f'Answer 2 is {cur_size}')