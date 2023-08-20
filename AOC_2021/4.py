# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:14:44 2021

@author: Eoin
"""


import math
import numpy as np
import pandas as pd

#test = np.loadtxt("4_test.txt", dtype = "str")

test = pd.read_csv("4_test.txt", sep="\n\n", header=None, engine = 'python')
input4 = pd.read_csv("4.txt", sep="\n\n", header=None, engine = 'python')

# drawn = pd.Series(test.loc[0,0].split(',')).astype(int)
# nboards = int((len(test)-1)/5)
# bingo = test.loc[1:,0].str.replace('  ', ' ').str.split(' ', expand=True).astype(int).reset_index(drop=True)

drawn = pd.Series(input4.loc[0,0].split(',')).astype(int)
nboards = int((len(input4)-1)/5)
bingo = input4.loc[1:,0].str.replace('  ', ' ').str.split(' ', expand=True).astype(int).reset_index(drop=True)


winner = -1
ndraws = 0

while (winner == -1):
    n = drawn[ndraws]
    ndraws += 1
    
    bingo[bingo == n] = np.nan # eliminate drawn no.
    
    for i in range(nboards):
        board = bingo.loc[5*i:4+(5*i),]
        
        #check columns
        for j in range(5):
            if board.iloc[:, j].isna().all():
                winner = i
                break
    
        #check rows
        for j in range(5):
            if board.iloc[j, :].isna().all():
                winner = i
                break

        # #check diags
        # if pd.Series([board.iloc[a,a] for a in range(5)]).isna().all():
        #     winner = i
        #     break
        # elif pd.Series([board.iloc[4-a,a] for a in range(5)]).isna().all():
        #     winner = i
        #     break


winningboard = bingo.loc[5*winner:4+(5*winner),].copy()

print(f'Answer 1 is {int(winningboard.sum().sum())*n}')



drawn = pd.Series(input4.loc[0,0].split(',')).astype(int)
nboards = int((len(input4)-1)/5)
bingo = input4.loc[1:,0].str.replace('  ', ' ').str.split(' ', expand=True).astype(int).reset_index(drop=True)

# drawn = pd.Series(test.loc[0,0].split(',')).astype(int)
# nboards = int((len(test)-1)/5)
# bingo = test.loc[1:,0].str.replace('  ', ' ').str.split(' ', expand=True).astype(int).reset_index(drop=True)


winners = set()
ndraws = 0

while (len(winners) < nboards-1):
    n = drawn[ndraws]
    ndraws += 1
    
    bingo[bingo == n] = np.nan # eliminate drawn no.
    
    for i in range(nboards):
        if i not in winners:
            board = bingo.loc[5*i:4+(5*i),]
            #check columns
            for j in range(5):
                if board.iloc[:, j].isna().all():
                    winners.add(i)
            #check rows
            for j in range(5):
                if board.iloc[j, :].isna().all():
                    winners.add(i)


loser = set(list(range(100))) - winners

losingboard = bingo.loc[5*list(loser)[0]:4+(5*list(loser)[0]),].copy()

winner = -1

while (winner == -1):
    n = drawn[ndraws]
    ndraws += 1
    
    losingboard[losingboard == n] = np.nan # eliminate drawn no.
    for j in range(5):
        if losingboard.iloc[:, j].isna().all():
            winner = 0
    #check rows
    for j in range(5):
        if losingboard.iloc[j, :].isna().all():
            winner = 0

print(f'Answer 2 is {int(losingboard.sum().sum())*n}')





# bingolist = []

# for i in range(nboards):
#     bingosquare = test.loc[1 + (5*i) : 5 + (5*i),0].\
#         str.replace('  ', ' ').str.split(' ', expand=True).astype(int)
#     rowindex = [f'{i}_{a}' for a in range(5)]
#     bingosquare.rename(index = rowindex, inplace=True)
    
#     bingolist.append(bingosquare)