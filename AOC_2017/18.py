# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 22:08:58 2023

@author: Eoin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

from collections import defaultdict

# [fname] = ["18_test.txt"]
[fname] = ["18.txt"]

with open(fname, "r") as file:
    sounds = file.read().splitlines()

reg = defaultdict(lambda : 0)

last_freq = 0
last_rec = 0

i = 0

while (0 <= i < len(sounds)) and last_rec == 0:
    snd = sounds[i]
    inst = snd.split(' ')
    [a, b] = [inst[0], inst[1]]
    
    if b[-1].isnumeric():
        val_b = int(b)
    else:
        val_b = reg[b]
        
    if len(inst) == 3:
        c = inst[2]
        if c[-1].isnumeric():
            val_c = int(c)
        else:
            val_c = reg[c]
        
    if a == 'jgz':
        if reg[b] > 0:
            i += val_c
        else:
            i += 1
    else:
        i += 1
    
        if a == 'snd':
            last_freq = reg[b]
        elif a == 'set':
            reg[b] = val_c
        elif a == 'add':
            reg[b] += val_c
        elif a == 'mul':
            reg[b] *= val_c
        elif a == 'mod':
            reg[b] = val_b%val_c
        elif a == 'rcv':
            if val_b != 0:
                last_rec = last_freq
    # print([i, snd, reg])
        

print(f'Answer 1 is {last_rec}')

[waiting_0, waiting_1, oob_0, oob_1] = [False, False, False, False]

q0 = [] # queue for number 1, from number 0
q1 = []

reg0 = defaultdict(lambda : 0)
reg1 = defaultdict(lambda : 0)
reg0['p'] = 0
reg1['p'] = 1

[i0, i1] = [0, 0]

total_sends = 0

def advance(i, q_send, q_rec, reg, int_id, total_sends):
    while (0 <= i < len(sounds)):
        snd = sounds[i]
        inst = snd.split(' ')
        [a, b] = [inst[0], inst[1]]
        
        if b[-1].isnumeric():
            val_b = int(b)
        else:
            val_b = reg[b]
            
        if len(inst) == 3:
            c = inst[2]
            if c[-1].isnumeric():
                val_c = int(c)
            else:
                val_c = reg[c]
            
        if a == 'jgz':
            if reg[b] > 0:
                i += val_c
            else:
                i += 1
        else:
            i += 1
        
            if a == 'snd':
                q_send.append(reg[b])
                if int_id == 1:
                    total_sends += 1
            elif a == 'set':
                reg[b] = val_c
            elif a == 'add':
                reg[b] += val_c
            elif a == 'mul':
                reg[b] *= val_c
            elif a == 'mod':
                reg[b] = val_b%val_c
            elif a == 'rcv':
                if len(q_rec) > 0:
                    new_val = q_rec.pop(0)
                    reg[b] = new_val
                else:
                    return(i, q_send, q_rec, reg, True, False, total_sends) # is waiting

        # print([i, snd, reg])
    
    return(i, q_send, q_rec, reg, False, True, total_sends) # is out of bounds


# 0 ok to run
# 0 not out of bounds AND (NOT waiting or WAITINg AND has data)


while ((not oob_0) and (not waiting_0 or len(q1)>0)) or ((not oob_1) and (not waiting_1 or len(q0)>0)):
    if (not waiting_0 and (not oob_0)):
        [i0, q0, q1, reg0, waiting_0, oob_0, _] = advance(i0, q0, q1, reg0, 0, 0)
    else:
        [i1, q1, q0, reg1, waiting_1, oob_1, total_sends] = advance(i1, q1, q0, reg1, 1, total_sends)


print(f'Answer 2 is {total_sends}')

from collections import defaultdict

f=open("18.txt",'r')
instr = [line.split() for line in f.read().strip().split("\n")]
f.close()

d1 = defaultdict(int) # registers for the programs
d2 = defaultdict(int)
d2['p'] = 1
ds = [d1,d2]

def get(s):
    if s in "qwertyuiopasdfghjklzxcvbnm":
        return d[s]
    return int(s)

tot = 0

ind = [0,0]         # instruction indices for both programs
snd = [[],[]]       # queues of sent data (snd[0] = data that program 0 has sent)
state = ["ok","ok"] # "ok", "r" for receiving, or "done"
pr = 0     # current program
d = ds[pr] # current program's registers
i = ind[0] # current program's instruction index
while True:
    if instr[i][0]=="snd": # send
        if pr==1: # count how many times program 1 sends
            tot+=1
        snd[pr].append(get(instr[i][1]))
    elif instr[i][0]=="set":
        d[instr[i][1]] = get(instr[i][2])
    elif instr[i][0]=="add":
        d[instr[i][1]] += get(instr[i][2])
    elif instr[i][0]=="mul":
        d[instr[i][1]] *= get(instr[i][2])
    elif instr[i][0]=="mod":
        d[instr[i][1]] %= get(instr[i][2])
    elif instr[i][0]=="rcv":
        if snd[1-pr]: # other program has sent data
            state[pr] = "ok"
            d[instr[i][1]] = snd[1-pr].pop(0) # get data
        else: # wait: switch to other prog
            if state[1-pr]=="done":
                break # will never recv: deadlock
            if len(snd[pr])==0 and state[1-pr]=="r":
                break # this one hasn't sent anything, other is recving: deadlock
            ind[pr] = i   # save instruction index
            state[pr]="r" # save state
            pr = 1 - pr   # change program
            i = ind[pr]-1 # (will be incremented back)
            d = ds[pr]    # change registers
    elif instr[i][0]=="jgz":
        if get(instr[i][1]) > 0:
            i+=get(instr[i][2])-1
    i+=1
    if not 0<=i<len(instr):
        if state[1-pr] == "done":
            break # both done
        state[pr] = "done"
        ind[pr] = i  # swap back since other program's not done
        pr = 1-pr
        i = ind[pr]
        d = ds[pr]

print(tot)
