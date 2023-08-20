# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 11:08:42 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

with open('11.txt', 'r') as file:
    items_input = file.read().splitlines()

# with open('11_test.txt', 'r') as file:
#     items_input = file.read().splitlines()

n = (len(items_input)+1)//7
monkeys = []

class monkey:
    def __init__(self, name, start_items, oper, test, dest_true, dest_false):
        self.name = name
        self.items = start_items
        self.oper = oper
        self.test = test
        self.dest_true = dest_true
        self.dest_false = dest_false
        self.n_inspect = 0
    
    def add_item(self, new_item):
        self.items.append(new_item)
    
    def inspection(self, worrydiv=True):
        for old in self.items:
            worry = eval(self.oper)
            #print(old, worry, worry//3, self.test)
            if worrydiv:
                worry = worry//3
            else:
                worry = worry%mega_mod
            
            if worry%self.test == 0:
                #print(f'throwing item {worry} to monkey {self.dest_true}')
                monkeys[self.dest_true].add_item(worry)
            else:
                monkeys[self.dest_false].add_item(worry)
            self.n_inspect += 1
        
        self.items = []

def monkey_items(monkeys):
    for j in range(len(monkeys)):
        print(j, monkeys[j].items)

for i in range(n):
    name = i
    items = items_input[7*i+1].split(': ')[-1].split(', ')
    items = [int(x) for x in items]
    oper = items_input[7*i+2].split(' = ')[-1]
    test = int(items_input[7*i+3].split(' by ')[-1])
    dest_true = int(items_input[7*i+4].split('monkey ')[-1])
    dest_false = int(items_input[7*i+5].split('monkey ')[-1])
    #print(name, items, oper, test, dest_true, dest_false)
    monkeys.append(monkey(name, items, oper, test, dest_true, dest_false))
    
def play(monkeys, rounds=20, log=True, worrydiv=True):
    for i in range(rounds):
        for j in range(len(monkeys)):
            monkeys[j].inspection(worrydiv)
        # if log:
        #     print(i, monkey_items(monkeys))
    
    activity = []
    for j in range(len(monkeys)):
        activity.append(monkeys[j].n_inspect)
    return activity
    
    if log:
        monkey_items(monkeys)
        
m_business = play(monkeys, rounds=20, log=True)
m_business.sort()
ans1 = m_business[-1] * m_business[-2]

print(f"Answer 1 is {ans1}")

monkeys = []
for i in range(n):
    name = i
    items = items_input[7*i+1].split(': ')[-1].split(', ')
    items = [int(x) for x in items]
    oper = items_input[7*i+2].split(' = ')[-1]
    test = int(items_input[7*i+3].split(' by ')[-1])
    dest_true = int(items_input[7*i+4].split('monkey ')[-1])
    dest_false = int(items_input[7*i+5].split('monkey ')[-1])
    #print(name, items, oper, test, dest_true, dest_false)
    monkeys.append(monkey(name, items, oper, test, dest_true, dest_false))

mega_mod = 1
for j in range(len(monkeys)):
    mega_mod *= monkeys[j].test


m_business = play(monkeys, rounds=10000, log=False, worrydiv=False)
m_business.sort()
ans2 = m_business[-1] * m_business[-2]

print(f"Answer 1 is {ans2}")
