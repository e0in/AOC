# -*- coding: utf-8 -*-
"""
Created on Sun May  1 17:22:36 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest


def parse_inst(fname):
    with open(fname, 'r') as file:
        inst = file.read().splitlines()
    
    inst_l = []
    for line in inst:
        line = line.split()
        if line[0] == 'swap':
            inst_l.append(['swap', line[2], line[5]])
        elif line[0] == 'reverse':
            inst_l.append(['reverse', line[2], line[4]])
        elif line[0] == 'move':
            inst_l.append(['move', line[2], line[5]])
        elif line[1] == 'based':
            inst_l.append(['rotate_on', line[6]])
        else:
            inst_l.append(['rotate_' + line[1], line[2]])
    
    return inst_l

test1 = parse_inst("21_test.txt")
inst = parse_inst("21.txt")

def scramble(passcode, inst):
    passcode = list(passcode)
    for line in inst:
        #print("".join(passcode), line)
        use_pos = line[1].isdigit()
        if use_pos:
            A = int(line[1])
            if len(line) == 3:
                B = int(line[2])
        else:
            A = passcode.index(line[1])
            if len(line) == 3:
                B = passcode.index(line[2])
        
        if line[0] == 'swap':
            temp = passcode[A]
            passcode[A] = passcode[B]
            passcode[B] = temp
        elif line[0] == 'reverse':
            passcode[A:B+1] = passcode[A:B+1][::-1]
        elif line[0] == 'rotate_left':
            passcode = passcode[A:] + passcode[:A]
        elif line[0] == 'rotate_right':
            passcode = passcode[-A:] + passcode[:-A]
        elif line[0] == 'move':
            temp = passcode[A]
            passcode = passcode[:A] + passcode[A+1:]
            passcode.insert(B, temp)
        else:
            ind = (A + 1 + int(A>=4))%len(passcode)
            print(A, ind)
            passcode = passcode[-ind:] + passcode[:-ind]
    return "".join(passcode)
            

#assert scramble("abcde", test1) == 'decab'
#print(f"Answer 1 is {scramble('abcdefgh', inst)}")

def unscramble(passcode, inst):
    passcode = list(passcode)
    for line in inst[::-1]:
        #print("".join(passcode), line)
        use_pos = line[1].isdigit()
        if use_pos:
            A = int(line[1])
            if len(line) == 3:
                B = int(line[2])
        else:
            A = passcode.index(line[1])
            if len(line) == 3:
                B = passcode.index(line[2])
        
        if line[0] == 'swap':
            temp = passcode[A]
            passcode[A] = passcode[B]
            passcode[B] = temp
        elif line[0] == 'reverse':
            passcode[A:B+1] = passcode[A:B+1][::-1]
        elif line[0] == 'rotate_left':
            passcode = passcode[-A:] + passcode[:-A]
        elif line[0] == 'rotate_right':
            passcode = passcode[A:] + passcode[:A]
        elif line[0] == 'move':
            A, B = B, A
            temp = passcode[A]
            passcode = passcode[:A] + passcode[A+1:]
            passcode.insert(B, temp)
        else:
            for i_old in range(len(passcode)):
                if A == (2*i_old + 1 + int(i_old>=4))%len(passcode):
                    ind = i_old - A
                    #print(ind, i_old)
                    continue
            #print(A, i_old, ind)
            if ind != 0:
                passcode = passcode[-ind:] + passcode[:-ind]
    return "".join(passcode)

#assert unscramble('decab', test1) == "abcde"
#assert unscramble('hcdefbag', inst) == 'abcdefgh'

# def unrotate(passcode, on):
#     passcode = list(passcode)
#     A = passcode.index(on)
        
#     for i_old in range(len(passcode)):
#         if A == (2*i_old + 1 + int(i_old>=4))%len(passcode):
#             ind = i_old - A
#             print(ind, i_old)
#             continue
#     #print(A, i_old, ind)
#     if ind != 0:
#         passcode = passcode[-ind:] + passcode[:-ind]

    
#     return "".join(passcode)


print(f"Answer 2 is {unscramble('fbgdceah', inst)}")