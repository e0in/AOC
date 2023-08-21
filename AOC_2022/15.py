# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 12:55:14 2022

@author: ehorgan
"""

# import math
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # Selector, put True for test data
# # [fname, y_trg, xy_max] = ["15_test.txt", 10, 20]
# [fname, y_trg, xy_max] = ["15.txt", 2000000, 4000000]

# with open(fname, 'r') as file:
#     sensors = file.read().splitlines()

# sx = []
# sy = []
# bx = []
# by = []
# rad = []
# ydist = []

# for line in sensors:
#     [s, b] = line.lstrip('Sensor at x=').split(': closest beacon is at x=')
#     s = [int(x) for x in s.split(', y=')]
#     sx.append(s[0])
#     sy.append(s[1])
#     b = [int(x) for x in b.split(', y=')]
#     bx.append(b[0])
#     by.append(b[1])
#     rad.append(abs(s[0] - b[0]) + abs(s[1] - b[1]))

# df = pd.DataFrame(list(zip(sx, sy, bx, by, rad)),
#                columns = ['sx', 'sy', 'bx', 'by', 'radius'])

# df['ydist'] = abs(y_trg - df['sy'])
# df['xdist'] = df['radius'] - df['ydist']
# #df['excl'] = None
# excl = []
# cov = []

# for i in range(len(df)):
#     if df.loc[i, 'xdist'] >= 0:
#         a = df.loc[i, 'sx'] - df.loc[i, 'xdist']
#         b = df.loc[i, 'sx'] + df.loc[i, 'xdist']
#         excl.append([a, b, b - a + 1])

# excl.sort()
# # covered_cells = excl[0][2]

# # for j in range(1, len(excl)):
# #     covered_cells += excl[j][2]
# #     covered_cells -= len(range(max(excl[j][0], excl[j+1][0]), min(excl[j][-1], excl[j+1][-1])+1))
# #     print(excl[j], covered_cells)
# # covered_cells += excl[j+1][1] - excl[j+1][0] + 1
# covered_cells = set(list(range(excl[0][0], excl[0][1])))
# for j in range(1, len(excl)):
#     new_cells = list(range(excl[j][0], excl[j][1]))
#     covered_cells = covered_cells.union(set(new_cells))

# print(f'Answer 1 is {len(covered_cells)}')  

# beacon_overall = np.ones([xy_max+1, xy_max+1], dtype=bool)

# for k in range(len(df)):
#     beacon_k = np.ones([xy_max+1, xy_max+1], dtype=bool)
#     r = df.loc[k, 'radius']
    
#     for i in range(xy_max+1):
#         for j in range(xy_max+1):
#             beacon_k[j, i] = abs(j-df.loc[k, 'sy']) + abs(i-df.loc[k, 'sx']) > r
    
#     beacon_overall = beacon_overall & beacon_k

# loc = np.where(beacon_overall)
# ypos = loc[0][0]
# xpos = loc[1][0]

# print(f'Answer 2 is {xpos*4000000 + ypos}')  

import sys


def parse_input(path):
    sensors = []
    for line in open(path):
        sx, sy, bx, by = [
            int(x.split('=')[1].rstrip(',:'))
            for x in line.split()
            if '=' in x
        ]
        sensors.append(((sx, sy), (bx, by)))
    return sensors


def merge_ranges(ranges):
    ranges.sort()
    overlaps = []
    merged = [ranges[0]]
    for thisl, thisr in ranges[1:]:
        prevl, prevr = merged[-1]
        if thisr <= prevr: # this sits entirely within prev
            pass
        elif thisl == prevl: # prev sits entirely within this
            merged[-1] = (thisl, thisr)
        elif thisl <= prevr + 1: # ranges can be merged
            overlaps.append(prevr - thisl + 1)
            merged[-1] = (prevl, thisr)
        else: # ranges do not overlap
            merged.append((thisl, thisr))
    return merged, min(overlaps) if overlaps else None


def get_coverage(sensors, y):
    ranges = []
    for (sx, sy), (bx, by) in sensors:
        coverage = abs(sx - bx) + abs(sy - by)
        ydist = abs(sy - y)
        if ydist > coverage:
            continue
        ranges.append((sx - (coverage - ydist),
                       sx + (coverage - ydist)))

    return merge_ranges(ranges)


def count_known_empty(sensors, y):
    coverage = get_coverage(sensors, y)[0]
    known_empty = 0
    beacons = {bx for _, (bx, by) in sensors if by == y}
    for l, r in coverage:
        n_beacons = len([b for b in beacons if l <= b <= r])
        known_empty += r - l + 1 - n_beacons
    return known_empty


def find_gap(sensors, minval, maxval):
    y = minval
    while True:
        ranges, internal_overlap = get_coverage(sensors, y)
        for l, r in ranges:
            if r < minval:
                continue
            if r < maxval:
                return 4000000 * (r + 1) + y
            if l > minval:
                return 4000000 * (l - 1) + y
            overlap = min(minval - l, r - maxval)
            break

        if internal_overlap:
            overlap = min(overlap, (internal_overlap + 1) // 2)
        y += overlap


def main(input_file):
    sensors = parse_input(input_file)
    print("Part 1:", count_known_empty(sensors, 2000000))
    print("Part 2:", find_gap(sensors, 0, 4000000))


if __name__ == '__main__':
    main("15.txt")