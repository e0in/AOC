# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:02:17 2022

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest
import time

fname = '17_test.txt'
# fname = '17.txt'

with open(fname, 'r') as file:
    jets = file.read().splitlines()

jets = [x == '<' for x in list(jets[0])] # True = Left, False = Right # %len(jets) to loop

cave = np.zeros([50, 7], dtype=bool)

rock1 = np.array([[True, True, True, True], [False, False, False, False],
                  [False, False, False, False], [False, False, False, False]])

rock2 = np.array([[False, True, False, False], [True, True, True, False], 
                  [False, True, False, False], [False, False, False, False]])

rock3 = np.array([[True, True, True, False], [False, False, True, False], 
                  [False, False, True, False], [False, False, False, False]])

rock4 = np.array([[True, False, False, False], [True, False, False, False],
                  [True, False, False, False], [True, False, False, False]])

rock5 = np.array([[True, True, False, False], [True, True, False, False],
                  [False, False, False, False], [False, False, False, False]])

rocktypes = [rock1, rock2, rock3, rock4, rock5]
rockw = [4, 3, 3, 1, 2] 
rockh = [1, 3, 3, 4, 2] 
rocks = [x.sum().sum() for x in rocktypes]

class falling_cave:
    def __init__(self, height, rocktypes, rockw, rockh, rocks, jets):
        self.state = np.zeros([height, 7], dtype=bool)
        self.rocktypes = rocktypes
        self.rockw = rockw
        self.rockh = rockh
        self.rocks = rocks
        self.jets = jets
        self.i = 0
        self.n_fell = 0
        self.ymax = 0
    
    def cur_state(self):
        return [self.n_fell, self.state]
    
    def fall(self, log = False):
        falling = True
        set_ex = False
        w = self.rockw[self.n_fell%len(self.rockw)]
        s = self.rocks[self.n_fell%len(self.rocks)]
        rock = self.rocktypes[self.n_fell%len(self.rocktypes)]
        x = 2
        y = self.ymax + 3
        while falling:
            left_dir = self.jets[self.i%len(self.jets)]
            print(x, y, left_dir, w)
            if left_dir and x > 0:
                # print(x, y, x-1, x+3)
                # print(self.state[y:y+4:,x-1:x+3])
                cur_count = self.state[y:y+4:,x-1:x+3].sum().sum()
                
                if x > 4:
                    new_count = np.add(self.state[y:y+4:,x-1:x+3], rock[:, 0:4-x]).sum().sum()
                else:
                    new_count = np.add(self.state[y:y+4:,x-1:x+3], rock).sum().sum()
                    
                if new_count == cur_count + s:
                    x -= 1
                    print(['Moved Left', x, y])
                else:
                    print(['Couldnt move Left', x, y])
            elif not left_dir and (x+w < 7):
                cur_count = self.state[y:y+4:,x+1:x+5].sum().sum()
                # print(x, y, w, x+1, x+5)
                # print(self.state[y:y+4:,x+1:x+5])
                if x > 2:
                    new_count = np.add(self.state[y:y+4:,x+1:x+5], rock[:, 0:6-x]).sum().sum()
                else:
                    new_count = np.add(self.state[y:y+4:,x+1:x+5], rock).sum().sum()
                    
                    
                if new_count == cur_count + s:
                    x += 1
                    print(['Moved Right', x, y])
                else:
                    print(['Couldnt move right', x, y])
            
            toprow = rock[0, :7-x]
            
            if y == 0:
                self.state[y:y+4:,x:x+4] = np.add(self.state[y:y+4:,x:x+4], rock[:, 0:7-x])
                falling = False
            elif (toprow & self.state[y-1, x:x+4]).any():
                self.state[y:y+4:,x:x+4] = np.add(self.state[y:y+4:,x:x+4], rock[:, 0:7-x])
                falling = False
            elif self.n_fell%len(self.rocktypes) == 1 and (rock[1, :7-x] & self.state[y-1, x:x+4]).any():
                #check line above for cross shape
                self.state[y-1:y+2:,x:x+3] = np.add(self.state[y-1:y+2:,x:x+3], rock[0:3, 0:3])
                falling = False
                set_ex = True
            else:
                y -= 1
                print('fell down one')

            self.i += 1
            # if log:
            #     plt.imshow(np.add(self.state[y:y+4:,x:x+4], rock[:, 0:7-x]), origin='lower')
            #     time.sleep(0.5)
            #     # print(self.state[self.ymax-4:self.ymax+6])
            
        h = self.rockh[self.n_fell%len(self.rockh)]
        self.n_fell += 1
        if y + h > self.ymax:
            self.ymax = y + h
            if set_ex:
                self.ymax -= 1
                set_ex = False
            print(f'set ymax to {self.ymax}')        
        print('Stopped')
        return 1
        
    def fall_n(self, n):
        for i in range(n):
            # print(f'fall {i+1}/{n}')
            self.fall()
        
part1 = falling_cave(3100, rocktypes, rockw, rockh, rocks, jets)
part1.fall_n(22)
part1.fall()
plt.imshow(part1.state[:part1.ymax], origin='lower')


print(f"Answer 1 is {part1.ymax}")


# print(f"Answer 2 is {ans2}")
