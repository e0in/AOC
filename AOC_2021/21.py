# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:17:17 2021

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd

# Selector, put True for test data
if False:
    [sp1, sp2] = [4, 8]
else:
    [sp1, sp2] = [10, 2]


class Player():
    def __init__(self, init_pos, limit=1000):
        self.pos = init_pos
        self.score = 0
        self.won = False
        self.limit = limit
        
    def inc(self, spaces):
        self.pos = (self.pos + spaces%10)//11 + (self.pos + spaces%10)%11
        # 4+6 = 10 # 8+15 = 3 # 7 + 69 = 6 # 4 + 276
        self.score += self.pos
        if self.score >= self.limit:
            self.won = True

P1 = Player(sp1)
P2 = Player(sp2)

det_die = np.arange(1,101)
die_long = np.tile(det_die, 20)
roll = 0

while (not P1.won) and (not P2.won):
    P1.inc(die_long[roll:roll+3].sum())
    #print(die_long[roll:roll+3])
    roll += 3
    if (not P1.won):
        P2.inc(die_long[roll:roll+3].sum())
        #print(die_long[roll:roll+3])
        roll += 3

if P1.won:
    ans1 = P2.score * roll
else:
    ans1 = P1.score * roll

print(f'Answer 1 is {ans1}')

n_player1 = 0
n_player2 = 0

spaces = [3, 4, 5, 6, 7, 8, 9]
univs  = [1, 3, 6, 7, 6, 3, 1]

# columns=['N', 'pos_1', 'score_1', 'pos_2', 'score_2', 'Player_1s_turn']

uni_state = [[1, sp1, 0, sp2, 0, True]]

while uni_state:
    [N, pos_1, score_1, pos_2, score_2, Player_1s_turn] = uni_state.pop()
    

    if Player_1s_turn:
        for i in range(7):
            new_pos = (pos_1 + spaces[i]%10)//11 + (pos_1 + spaces[i]%10)%11
            new_score = score_1 + new_pos
            if new_score >= 21:
                n_player1 += N*univs[i]
            else:
                new_unis = [N*univs[i], new_pos, new_score, pos_2, score_2, False]
                uni_state.append(new_unis)
    else:
        for i in range(7):
            new_pos = (pos_2 + spaces[i]%10)//11 + (pos_2 + spaces[i]%10)%11
            new_score = score_2 + new_pos
            if new_score >= 21:
                n_player2 += N*univs[i]
            else:
                new_unis = [N*univs[i], pos_1, score_1, new_pos, new_score, True]
                uni_state.append(new_unis)
                        
    
    
print(f'Answer 2 is {max([n_player1, n_player2])}')
    
    