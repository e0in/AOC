# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:24:12 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

player_hp = 50; player_arm = 0; mana = 500

boss_hp = 51; boss_dam = 9

# [player_hp, mana, boss_hp, shield, poison, recharge, turns, mana_spent]
state = [player_hp, player_hp, player_arm, mana, boss_hp, 0, 0, 0, 0, 0]
all_states = [state]

# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

min_mana = 1000000
min_mana_hard = 1000000

while all_states:
    [player_hp, player_hp_hard, player_arm, mana, boss_hp, shield, poison, recharge, turns, mana_spent] = all_states.pop()
    print([len(all_states), player_hp, player_hp_hard, boss_hp, turns, min_mana, min_mana_hard])
    
    if (not bool(turns%2)):
        player_hp_hard -= 1
    
    if shield > 0:
        shield -= 1
        if shield == 0:
            player_arm = 0

    if poison > 0:
        poison -= 1
        boss_hp -= 3
        if boss_hp <= 0:
            if mana_spent < max(min_mana, min_mana_hard):
                min_mana = mana_spent #print('died of poison')
            if player_hp_hard > 0:
                if mana_spent < min_mana_hard:
                    min_mana_hard = mana_spent
            continue
        
    if recharge > 0:
        recharge -= 1
        mana += 101
    
    turns += 1
    if bool(turns%2): # Players turn
    
        if mana >= 229 and recharge == 0:
            if mana_spent+229 < max(min_mana, min_mana_hard):
                all_states.append([player_hp, player_hp_hard, player_arm, mana-229, boss_hp, shield, poison, 5, turns, mana_spent+229])
        
        if mana >= 113 and shield == 0:
            if mana_spent+113 < max(min_mana, min_mana_hard):
                all_states.append([player_hp, player_hp_hard, 7, mana-113, boss_hp, 6, poison, recharge, turns, mana_spent+113])
        
        if mana >= 73:
            new_boss_hp = boss_hp - 2
            if new_boss_hp <= 0:
                if mana_spent+73 < min_mana:
                    min_mana = mana_spent+73
                if player_hp_hard > 0:
                    if mana_spent+73 < min_mana_hard:
                        min_mana_hard = mana_spent+73
                continue
            else:
                if mana_spent+73 < max(min_mana, min_mana_hard):
                    all_states.append([player_hp+2, player_hp_hard+2, player_arm, mana-73, new_boss_hp, shield, poison, recharge, turns, mana_spent+73])
        
        if mana >= 53:
            new_boss_hp = boss_hp - 4
            if new_boss_hp <= 0:
                if mana_spent+53 < min_mana:
                    min_mana = mana_spent+53
                if player_hp_hard > 0:
                    if mana_spent+53 < min_mana_hard:
                        min_mana_hard = mana_spent+53
                continue
            else:
                if mana_spent+53 < max(min_mana, min_mana_hard):
                    all_states.append([player_hp, player_hp_hard, player_arm, mana-53, new_boss_hp, shield, poison, recharge, turns, mana_spent+53])
            
        if mana >= 173 and poison == 0:
            if mana_spent+173 < max(min_mana, min_mana_hard):
                all_states.append([player_hp, player_hp_hard, player_arm, mana-173, boss_hp, shield, 6, recharge, turns, mana_spent+173])
            
            
    else: #bosses turn
        boss_hit = max(1, boss_dam - player_arm)
        player_hp -= boss_hit
        player_hp_hard -= boss_hit
        if player_hp > 0:
            all_states.append([player_hp, player_hp_hard, player_arm, mana, boss_hp, shield, poison, recharge, turns, mana_spent])

                

print(f'Answer 1 is {min_mana}')
print(f'Answer 2 is {min_mana_hard}')