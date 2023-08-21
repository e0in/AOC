# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:44:35 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

player_hp = 100; player_dam = 0; player_arm = 0

boss_hp = 104; boss_dam = 8; boss_arm = 1

shop = pd.read_csv("21.txt", sep='\n', header=None, engine='python')

for i in range(len(shop)):
    row = shop.loc[i, :]
    shop.loc[i, :] = ' '.join(row[0].split())

shop = shop[0].str.split(' ', expand=True)

arm_ind = shop.index[shop[0] == 'Armor:'][0]
ring_ind = shop.index[shop[0] == 'Rings:'][0]

shop.columns = ['name', 'cost', 'damage', 'armor']

weapons = shop.loc[1:arm_ind-1, :].copy().reset_index(drop=True)
weapons[['cost', 'damage', 'armor']] = weapons[['cost', 'damage', 'armor']].astype(int)

armor = shop.loc[arm_ind+1:ring_ind-1, :].copy().reset_index(drop=True)
armor[['cost', 'damage', 'armor']] = armor[['cost', 'damage', 'armor']].astype(int)
armor.loc[len(armor), :] = ['None', 0, 0, 0]

rings = shop.loc[ring_ind+1:, :].copy().reset_index(drop=True)
rings[['cost', 'damage', 'armor']] = rings[['cost', 'damage', 'armor']].astype(int)
rings.loc[len(rings), :] = ['None1', 0, 0, 0]
rings.loc[len(rings), :] = ['None2', 0, 0, 0]


min_cost = 1000000
max_cost = 0

for i in range(len(weapons)):
    w = weapons.loc[i, :]
    
    for j in range(len(armor)):
        a = armor.loc[j, :]
        
        for k in range(len(rings)-1):
            r1 = rings.loc[k, :]
            
            for l in range(k+1, len(rings)):
                r2 = rings.loc[l, :]
                
                cost = w['cost'] + a['cost'] + r1['cost'] + r2['cost']
                player_dam = w['damage'] + r1['damage'] + r2['damage']
                player_arm = a['armor'] + r1['armor'] + r2['armor']

                
                player_hit = max(1, player_dam - boss_arm)
                boss_kill = boss_hp//player_hit + int(bool(boss_hp%player_hit))
                
                boss_hit = max(1, boss_dam - player_arm)
                player_kill = player_hp//boss_hit + int(bool(player_hp%boss_hit))
                
                if boss_kill <= player_kill:
                    if cost < min_cost:
                        min_cost = cost
                else:
                    if cost > max_cost:
                        max_cost = cost

print(f'Answer 1 is {min_cost}')
print(f'Answer 2 is {max_cost}')