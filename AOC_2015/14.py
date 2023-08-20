# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 19:10:17 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd

if True:
    fname = "14.txt"
    time = 2503
else:
    fname = "14_test.txt"
    time = 1000

df = pd.read_csv(fname, sep=" can fly ", header=None, engine='python', names = ['name', 'p2'])

df['p2'] = df['p2'].str.rstrip('.')
df[['vel', 'dur', 'rest']] = df['p2'].str.split(expand=True)[[0, 3, 10]].astype(int)

df = df[['name', 'vel', 'dur', 'rest']]

df['dist'] = df['vel'] * df['dur']
df['cyc'] = df['dur'] + df['rest']

# def print_dist(df, time):
#     for i in range(len(df)):
#         deer = df.loc[i, :]
#         tot_dist = (deer.dist * (time // deer.cyc)) + min(deer.dist, deer.vel * (time % deer.cyc))
#         print([deer['name'], tot_dist])
        
#print_dist(df, 1000)

def rein_dist(time, dist, cyc, vel):
    return (dist * (time // cyc)) + min(dist, vel * (time % cyc))


for i in range(len(df)):
    deer = df.loc[i, :]
    df.loc[i, 'tot_dist'] = rein_dist(time, deer.dist, deer.cyc, deer.vel)


print(f'Answer 1 is {int(df.tot_dist.max())}')



vec_rein_dist = np.vectorize(rein_dist)

dist_arr = np.zeros([time, len(df)], dtype = int)

for i in range(len(df)):
    deer = df.loc[i, :]
    dist_arr[:, i] = vec_rein_dist(np.arange(time), deer.dist, deer.cyc, deer.vel)
    
dist_arr = np.delete(dist_arr, 0, 0)
dist_max = np.amax(dist_arr, axis=1)
point_max = 0

for i in range(len(df)):
    points = sum(dist_arr[:, i] == dist_max)
    if points > point_max:
        point_max = points

print(f'Answer 2 is {point_max}')












# class Reindeer:
#   def __init__(self, name, vel, dur, rest):
#     self.name = name
#     self.vel = vel
#     self.dur = dur
#     self.rest = rest
#     self.dist = 0
#     self.runtime = dur
#     self.resttime = 0