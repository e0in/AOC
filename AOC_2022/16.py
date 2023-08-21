# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 09:06:56 2022

@author: ehorgan
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import itertools
# from tqdm import tqdm
import heapq

# Selector, put True for test data
# [fname] = ["16_test.txt"]
[fname] = ["16.txt"]

G = nx.Graph()
fv = ['AA']
flow_list = [0]
flow_dict = {'AA': 0}

with open(fname, 'r') as file:
    valves = file.read().splitlines()

for valve in valves:
    [name, b] = valve.lstrip('Valve ').split(' has flow rate=')
    [flow, c] = b.split(';')
    flow = int(flow)
    if flow > 0:
        fv.append(name)
        flow_list.append(flow)
        flow_dict[name] = flow
        
    conn = c.split('valve')[-1].lstrip('s ').split(', ')
    # print(name, flow, conn)
    G.add_node(name, flow=flow)
    G.add_edges_from([(name, x) for x in conn], weight=1)
    # G.nodes['AA']['flow']

nx.draw(G, with_labels=True, font_weight='bold')
ap = nx.shortest_path_length(G, source='AA', target=None)
new_ap = {k: ap[k] for k in fv if k in ap}

df = pd.DataFrame(new_ap.values(), index = new_ap.keys(), columns=['AA'])

for source in fv[1:]:
    sp = nx.shortest_path_length(G, source=source, target=None)
    new_sp = {k: sp[k] for k in fv if k in sp}
    df[source] = new_sp.values()

def traverse_valves(df, order, flow_dict):
    [cur_flow, tot_flow, time, i] = [0, 0, 0, 0]
    while time <= 30 and i < len(order)-1:
        journey = df[order[i]][order[i+1]] + 1
        i += 1
        if time + journey > 30:
            tot_flow += (30-time) * cur_flow
        else:
            tot_flow += journey * cur_flow
            cur_flow += flow_dict[order[i]]
        time += journey
    
    if time <= 30:
        tot_flow += (30-time) * cur_flow
        
    return [tot_flow, 30-time]

# max_flow = 0

# Q = [['AA', x] for x in fv[1:]]

# while Q:
#     order = Q.pop()
#     [ord_flow, ret_time] = traverse_valves(df, order, flow_dict)
#     if ord_flow > max_flow:
#         max_flow = ord_flow
#         print(max_flow, order)
#     if ret_time > 0:
#         pos_trgts = [value for value in fv if (value not in order) and (df[value][order[-1]] + 1 < ret_time)]
#         Q += [order + [x] for x in pos_trgts]

# # for order in list(itertools.permutations(fv[1:])):
# #     full_order = ['AA'] + list(order)
# #     ord_flow = traverse_valves(df, full_order, flow_dict)
# #     if ord_flow > max_flow:
# #         max_flow = ord_flow

# print(f'Answer 1 is {max_flow}')

def traverse_elephant(df, order_m, order_e, flow_dict, time_lim=26):
    [time, time2, i, j] = [0, 0, 0, 0]
    
    arr_m = np.zeros(time_lim, dtype=int)
    arr_e = np.zeros(time_lim, dtype=int)
    
    while time <= time_lim and i < len(order_m)-1:
        arr_m[time] = flow_dict[order_m[i]]
        journey = df[order_m[i]][order_m[i+1]] + 1
        i += 1
        time += journey
    if time < time_lim and i < len(order_m):
        arr_m[time] = flow_dict[order_m[i]]
        
    while time2 <= time_lim and j < len(order_e)-1:
        arr_e[time2] = flow_dict[order_e[j]]
        journey = df[order_e[j]][order_e[j+1]] + 1
        j += 1
        time2 += journey
    if time2 < time_lim and j < len(order_e):
        arr_e[time2] = flow_dict[order_e[j]]
        
    tot_flow = np.cumsum(arr_m + arr_e).sum()
        
    return [tot_flow, time_lim-time, time_lim-time2]

# traverse_elephant(df, ['AA', 'JJ', 'BB', 'CC'], ['AA', 'DD', 'HH', 'EE'], flow_dict, time_lim=26) = [1707, 17, 15]

# pos_trgts = fv[1:]
max_flow = 0
Q = []
for init_dests in list(itertools.permutations(fv[1:], 2)):
    [dest_m, dest_e] = init_dests
    pos_trgts = [value for value in fv[1:] if (value not in init_dests)]
    heapq.heappush(Q, (0, ['AA', dest_m], ['AA', dest_e], pos_trgts))
# t_tot = len(Q)
# done = 0

# t = tqdm(total=1)

while Q:
    [_, order_m, order_e, rem_valves] = heapq.heappop(Q)
    # print([order_m, order_e, rem_valves])
    [ord_flow, ret_time, ret_time2] = traverse_elephant(df, order_m, order_e, flow_dict)
    # done += 1
    if ord_flow > max_flow:
        max_flow = ord_flow
        print(max_flow, len(Q), order_m, order_e)
    if ret_time > 0 and ret_time2 > 0:
        for next_dests in list(itertools.permutations(rem_valves, 2)):
            [dest_m, dest_e] = next_dests
            pos_trgts = [value for value in rem_valves if (value not in next_dests)]
            heapq.heappush(Q, (-ord_flow, order_m + [dest_m], order_e + [dest_e], pos_trgts))

            # t_tot += 1
        #Q += [order + [x] for x in pos_trgts]
    elif ret_time > 0:
        for next_dest in list(itertools.permutations(rem_valves, 1)):
            pos_trgts = [value for value in rem_valves if (value not in next_dest)]
            heapq.heappush(Q, (-ord_flow, order_m + [next_dest[0]], order_e, pos_trgts))
            # t_tot += 1
    elif ret_time2 > 0:
        for next_dest in list(itertools.permutations(rem_valves, 1)):
            pos_trgts = [value for value in rem_valves if (value not in next_dest)]
            heapq.heappush(Q, (-ord_flow, order_m, order_e + [next_dest[0]], pos_trgts))
#             t_tot += 1
#     t.update(done/t_tot)
# t.close()

print(f'Answer 2 is {max_flow}')

# from dataclasses import dataclass
# from copy import copy
 
# INF = int(1e9)
 
 
# @dataclass
# class Valve:
#     name: str
#     flow_rate: int
#     children: list[str]
 
 
# def parse_input():
#     with open(INPUT_FILENAME, "r") as file:
#         lines = [l.rstrip() for l in file.readlines()]
 
#     valves = {}
 
#     for line in lines:
#         split = line.split(" ")
#         valve_name = split[1]
#         flow_rate = int(split[4][:-1].split("=")[1])
#         children = [split[-1]] + [token[:-1] for token in split if token.endswith(",")]
#         valves[valve_name] = Valve(valve_name, flow_rate, children)
 
#     return valves
 
 
# def floid_warshall(valves):
#     dist = {v: {u: INF for u in valves} for v in valves}
 
#     for v in valves:
#         dist[v][v] = 0
#         for u in valves[v].children:
#             dist[v][u] = 1
 
#     for k in valves:
#         for i in valves:
#             for j in valves:
#                 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
 
#     return dist
 
 
# def main():
#     valves = parse_input()
#     distances = floid_warshall(valves)
#     non_zero_valves = [v for v in valves if valves[v].flow_rate > 0]
 
#     def generate_open_options(pos, open_valves, time_left):
#         for next in non_zero_valves:
#             if next not in open_valves and distances[pos][next] < time_left:
#                 open_valves.append(next)
#                 yield from generate_open_options(
#                     next, open_valves, time_left - distances[pos][next] - 1
#                 )
#                 open_valves.pop()
 
#         yield copy(open_valves)
 
#     def get_order_score(open_order, time_left):
#         now, ans = "AA", 0
#         for pos in open_order:
#             time_left -= distances[now][pos] + 1
#             ans += valves[pos].flow_rate * time_left
#             now = pos
#         return ans
 
#     def solution_1():
#         return max(get_order_score(o, 30) for o in generate_open_options("AA", [], 30))
 
#     def solution_2():
#         ways = list(generate_open_options("AA", [], 26))
 
#         best_scores = {}
 
#         for order in ways:
#             tup = tuple(sorted(order))
#             score = get_order_score(order, 26)
#             best_scores[tup] = max(best_scores.get(tup, 0), score)
 
#         best_scores = list(best_scores.items())
        
#         print(len(best_scores))
#         print(len(ways))
 
#         ans = 0
#         for human_idx in range(len(best_scores)):
#             for elephant_idx in range(human_idx + 1, len(best_scores)):
#                 human_opens, human_score = best_scores[human_idx]
#                 elephant_opens, elephant_score = best_scores[elephant_idx]
 
#                 if len(set(human_opens).intersection(elephant_opens)) == 0:
#                     ans = max(ans, human_score + elephant_score)
 
#         return ans
 
#     print("Answer 1:", solution_1())
#     print("Answer 2:", solution_2())
 
 
# if __name__ == "__main__":
#     INPUT_FILENAME = "16.txt"
#     main()