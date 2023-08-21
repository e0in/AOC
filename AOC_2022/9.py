# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:27:26 2022

@author: ehorgan
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Selector, put True for test data
if False:
    fname = "9_test2.txt"
else:
    fname = "9.txt"


with open(fname, 'r') as file:
    rope = file.read().splitlines()

rope = [[x.split()[0], int(x.split()[1])] for x in rope]

t_loc = []

head = [0, 0] # x, y
tail = [0, 0]

for i in range(len(rope)):
    [direc, val] = rope[i]
    
    for i in range(val):
        if direc == 'R':
            head[0] += 1
        elif direc == 'L':
            head[0] -= 1
        elif direc == 'U':
            head[1] += 1
        elif direc == 'D':
            head[1] -= 1
        # print(head)
        
        xd = head[0] - tail[0]
        yd = head[1] - tail[1]
        
        manhat = abs(xd) + abs(yd)
        
        if manhat < 2:
            pass
        elif manhat == 2:
            if (xd)**2 + (yd)**2 == 4:
                if head[0] != tail[0]:
                    if xd > 0:
                        tail[0] += 1
                    else:
                        tail[0] -= 1
                else:
                    if yd > 0:
                        tail[1] += 1
                    else:
                        tail[1] -= 1
        else:
            if (xd > 0) and (yd > 0):
                tail = [tail[0] + 1, tail[1] + 1]
            elif (xd > 0) and (yd < 0):
                tail = [tail[0] + 1, tail[1] - 1]
            elif (xd < 0) and (yd > 0):
                tail = [tail[0] - 1, tail[1] + 1]
            else:
                tail = [tail[0] - 1, tail[1] - 1]
            
        # print([head, tail, xd, yd, manhat, (xd)**2 + (yd)**2])
        t_loc.append((tail[0], tail[1]))

        
print(f'Answer 1 is {len(set(t_loc))}')

t_loc = []

x = 10*[0]
y = 10*[0]

#rope = rope[0:2]

for i in range(len(rope)):
    [direc, val] = rope[i]
    
    for i in range(val):
        if direc == 'R':
            x[0] += 1
        elif direc == 'L':
            x[0] -= 1
        elif direc == 'U':
            y[0] += 1
        elif direc == 'D':
            y[0] -= 1
        # print(head)
        
        for j in range(1, 10):
            xd = x[j-1] - x[j]
            yd = y[j-1] - y[j]
            
            manhat = abs(xd) + abs(yd)
            
            if manhat < 2:
                pass
            elif manhat == 2:
                if (xd)**2 + (yd)**2 == 4:
                    if x[j] != x[j-1]:
                        if xd > 0:
                            x[j] += 1
                        else:
                            x[j] -= 1
                    else:
                        if yd > 0:
                            y[j] += 1
                        else:
                            y[j] -= 1
            else:
                if (xd > 0) and (yd > 0):
                    x[j] += 1
                    y[j] += 1
                elif (xd > 0) and (yd < 0):
                    x[j] += 1
                    y[j] -= 1
                elif (xd < 0) and (yd > 0):
                    x[j] -= 1
                    y[j] += 1
                else:
                    x[j] -= 1
                    y[j] -= 1
            #print([x, y, xd, yd, manhat, (xd)**2 + (yd)**2])
                
        #print([x, y, xd, yd, manhat, (xd)**2 + (yd)**2])
        t_loc.append((x[9], y[9]))

        
print(f'Answer 2 is {len(set(t_loc))}')
