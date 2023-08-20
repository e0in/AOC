# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:25:03 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

with open('10.txt', 'r') as file:
    inst = file.read().splitlines()

#bots = pd.read_csv("10_test.txt", sep=",", header=None, names = ["txt"], engine='python')

class botlist:
    def __init__(self):
        self.bots = dict()
        self.outs = dict()
        self.compbot = None
    
    def add(self, bot, chip):
        if bot not in self.bots.keys():
            self.bots[bot] = [chip]
        else:
            if len(self.bots[bot]) > 1:
                raise ValueError('Max two chips per bot')
            else:
                self.bots[bot] = sorted([chip] + self.bots[bot])
                
                if self.bots[bot] == [17, 61]:
                    self.compbot = bot
    
    def send(self, output, chip):
        if output not in self.outs.keys():
            self.outs[output] = [chip]
        else:
            self.outs[output].append(chip)
        
    def transfer(self, comp):
        bot = comp[0]
        for i in [0, 1]:
            [dest_type, dest] = comp[1+i].split(' ')
            dest = int(dest)
            if dest_type == 'output':
                self.send(dest, self.bots[bot][i])
            else:
                self.add(dest, self.bots[bot][i])
        
        del(self.bots[bot])
            

bunny_bots = botlist()

comps = []
for line in inst:
    if line[:5] == 'value':
        [val, bot] = [int(x) for x in line[6:].split(' goes to bot ')]
        bunny_bots.add(bot, val)
    else:
        [a, b] =  line[4:].split(' gives low to ')
        [b, c] = b.split(' and high to ')
        comps.append([int(a), b, c])

while comps:
    comp = comps.pop(0)
    if comp[0] in bunny_bots.bots.keys():
        if len(bunny_bots.bots[comp[0]]) == 2:
            bunny_bots.transfer(comp)
        else:
            comps.append(comp)
    else:
        comps.append(comp)
    

    
print(f'Answer 1 is {bunny_bots.compbot}')


print(f'Answer 2 is {bunny_bots.outs[0][0] * bunny_bots.outs[1][0] * bunny_bots.outs[2][0]}')