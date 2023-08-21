# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:42:31 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

test = pd.read_csv("13_test.txt", header=None, dtype = "str")
input13 = pd.read_csv("13.txt", header=None, dtype = "str")

# Selector, put True for test data
if False:
    df = test
else:
    df = input13

coords = df[~df[1].isna()].astype(int)
inst = df.loc[df[1].isna(), 0].str.replace("fold along", "").str.split("=", expand = True)

def create_matrix(coords):
    mat = pd.DataFrame(np.zeros([(coords.max()+1)[1], (coords.max()+1)[0]]), dtype=bool)
    for i in range(len(coords)):
        mat.loc[coords.loc[i, 1], coords.loc[i, 0]] = True
    return(mat)

def fold(coords, inst, nfolds):
    for i in range(nfolds):
        fold_dir = inst.iloc[i, 0]
        fold = int(inst.iloc[i, 1])
        if fold_dir == ' y':
            dy = (coords[1]-fold).copy()
            dy[dy<0] = 0           
            coords[1] -= (2*dy)
        else:
            dx = (coords[0]-fold).copy()
            dx[dx<0] = 0                
            coords[0] -= (2*dx)
    
    return(coords)


mat1 = create_matrix(fold(coords.copy(), inst, 1))

print(f'Answer 1 is {mat1.sum().sum()}') 


mat2 = create_matrix(fold(coords, inst, len(inst)))

plt.imshow(mat2)
