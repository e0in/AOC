# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:05:21 2021

@author: Eoin
"""

import math
import numpy as np
import pandas as pd

# True for test data
if False:
    trgt = [20, 30, -10, -5] # xmin, xmax, ymin, ymax
    xrange = range(0, 40, 1)
    yrange = range(-20, 30, 1)
else:
    trgt = [150, 193, -136, -86]
    xrange = range(0, 200, 1)
    yrange = range(-140, 150, 1)
    

class Probe:
    def __init__(self, trgt, v):
        self.trgt = trgt
        self.x = 0
        self.y = 0
        self.xv = v[0]
        self.yv = v[1]
        self.alt = 0
        self.hit = False
    
    def sim(self):
        while (self.y > self.trgt[2]):
            self.x += self.xv
            self.y += self.yv
            
            if self.xv > 0:
                self.xv -= 1
            elif self.xv < 0:
                self.xv += 1
            self.yv -= 1
            
            #print([self.x, self.y, self.xv, self.yv])
            
            if self.y > self.alt:
                self.alt = self.y
                
            if (self.trgt[0] <= self.x <= self.trgt[1]) and (self.trgt[2] <= self.y <= self.trgt[3]):
                #print('hit')
                self.hit = True
                
        if self.hit:
            return(self.alt)
        else:
            return(-9999)

ymax = 0
bestv = [0, 0]
count = 0

for i in xrange:
    for j in yrange:
        probe = Probe(trgt, [i, j])
        alt = probe.sim()
        if probe.hit:
            count += 1
            if alt > ymax:
                ymax = alt
                bestv = [i, j]
            

print(f'Answer 1 is {ymax}')
print(f'Answer 2 is {count}')
            
            