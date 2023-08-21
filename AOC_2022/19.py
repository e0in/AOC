# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 10:47:47 2022

@author: ehorgan
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import heapq
import re

# Selector, put True for test data
# [fname] = ["19_test.txt"]
[fname] = ["19.txt"]

with open(fname, 'r') as file:
    robots_bp = file.read().splitlines()

factory = []
for line in robots_bp:
    factory.append([int(x) for x in re.findall(r'\d+', line)])

max_geodes = []
cache = set()
    
for bp in factory:
    # k = 0
    res = [0, 0, 0, 0] # ore, clay, obsidian, geode
    robots =  [1, 0, 0, 0] # ore, clay, obsidian, geode

    Q = [(0, res, robots)]
    max_g = 0
    geodes = []
    
    while Q:
        # k += 1
        curr = heapq.heappop(Q)
        if curr not in cache:
            cache.add(curr)
            [time, res, robots] = curr
            can_build = [res[0] >= bp[1], res[0] >= bp[2],
                        (res[0] >= bp[3]) and (res[1] >= bp[4]),
                        (res[0] >= bp[5]) and (res[2] >= bp[6])]
            
            for i in range(4):
                res[i] += robots[i]
            
            time -= 1
            
            # rem_turns = 24 + time
            
            if time == -24:
                if res[3] > max_g:
                    max_g = res[3]
                    print(f'Completed search, id={bp[0]}, geodes={res[3]}')#, iteration={k}
                
            else:
                if not all(can_build):
                    heapq.heappush(Q, (time, res, robots))
                    
                if can_build[0] and not can_build[3]:
                    heapq.heappush(Q, (time, [res[0] - bp[1], res[1], res[2], res[3]],
                                        [robots[0] + 1, robots[1], robots[2], robots[3]]))
                if can_build[1] and not can_build[3]:
                    heapq.heappush(Q, (time, [res[0] - bp[2], res[1], res[2], res[3]],
                                        [robots[0], robots[1] + 1, robots[2], robots[3]]))
                if can_build[2] and not can_build[3]:
                    heapq.heappush(Q, (time, [res[0] - bp[3], res[1] - bp[4], res[2], res[3]],
                                        [robots[0], robots[1], robots[2] + 1, robots[3]]))
                if can_build[3]:
                    heapq.heappush(Q, (time, [res[0] - bp[5], res[1], res[2] - bp[6], res[3]],
                                        [robots[0], robots[1], robots[2], robots[3] + 1]))
            
            # if time == time_lim:
            #     geodes.append([res[3], bp[0]])
            # else:
            #     if can_build[3]:
            #         heapq.heappush(Q, (time, [res[0] - bp[5], res[1], res[2] - bp[6], res[3]],
            #                            [robots[0], robots[1], robots[2], robots[3] + 1]))
            #     elif can_build[2]:
            #         heapq.heappush(Q, (time, [res[0] - bp[3], res[1] - bp[4], res[2], res[3]],
            #                            [robots[0], robots[1], robots[2] + 1, robots[3]]))
            #     elif can_build[1]:
            #         heapq.heappush(Q, (time, [res[0] - bp[2], res[1], res[2], res[3]],
            #                            [robots[0], robots[1] + 1, robots[2], robots[3]]))
            #     elif can_build[0]:
            #         heapq.heappush(Q, (time, [res[0] - bp[1], res[1], res[2], res[3]],
            #                            [robots[0] + 1, robots[1], robots[2], robots[3]]))
            #     else:
            #         heapq.heappush(Q, (time, res, robots))
    
    max_geodes.append([bp[0], max_g])  
    
quality = [x[0]*x[1] for x in max_geodes]

print(f'Answer 1 is {sum(quality)}')

# print(f'Answer 2 is {max_flow}')
