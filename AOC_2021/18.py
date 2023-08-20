# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 10:51:29 2021

@author: Eoin
"""

import math
import numpy as np
import pandas as pd

test1 = pd.read_csv("18_test_1.txt", sep=" ", header=None)
test2 = pd.read_csv("18_test_2.txt", sep=" ", header=None)
inputdat = pd.read_csv("18.txt", sep=" ", header=None)

data = 3
if data == 1:
    df = test1
elif data ==2:
    df = test2
else:
    df = inputdat


def snail_explode(strA):
    has_explode = False
    strB = []
    brackets = []
    depth = 0
    addright = 0        
    
    i = 0
    while i < len(strA):
        char = strA[i]
        if char == '[':
            depth += 1
            brackets.append(char)
        elif char == ']':
            depth -= 1
            brackets.append(char)
        elif char == ',':
            brackets.append(char)
        else:
            if strA[i+1].isnumeric():
                ichar = int(strA[i:i+2])
                char = str(ichar)
                i += 1
            else:
                ichar = int(char)
                
            if addright > 0:#rightwards explode
                char = str(ichar + addright)
                addright = 0
            
            if depth <= 4 or has_explode:
                strB += brackets
                brackets = []
                strB.append(char)
            else:
                if len(strB) > 0:
                    strB[-1] = str(int(strB[-1]) + ichar)
                i += 2
                #print([i, strA[i], strA, strA[0:i]])
                
                if strA[i+1].isnumeric():
                    addright = int(strA[i:i+2])
                    i += 1
                else:
                    addright = int(strA[i])
                
                brackets.pop()
                strB += brackets
                brackets = []
                strB.append('0')
                i += 1
                depth -= 1
                has_explode = True
        
        i += 1
    strB += brackets
    return ("".join(strB))

def snail_split(strB):
    has_split = False
    strC = []
    i = 0
    while i < len(strB):
        char = strB[i]
        if char.isnumeric() and (not has_split):
            n = [char]
            i += 1
            while strB[i].isnumeric():
                n.append(strB[i])
                i += 1
            val = int("".join(n))
            if val > 9:
                strC += ['[', str(math.floor(val/2)), ',', str(math.ceil(val/2)), ']']
                has_split = True
            else:
                strC.append(str(val))
            
        else:
            strC.append(char)
            i += 1
    return("".join(strC))

def snail_reduce(instr):
    instr

    
    splits_left = True
    explodes_left = True
    
    while splits_left or explodes_left:
        while explodes_left:
            str_temp = snail_explode(instr)
            if str_temp == instr:
                explodes_left = False
            else:
                instr = str_temp
                # print('exploded: ' + instr)
                
        if splits_left:
            str_temp = snail_split(instr)
            if str_temp == instr:
                splits_left = False
            else:
                instr = str_temp
                # print('split: ' + instr)
                explodes_left = True
        
    
    return(instr)

def snail_add(str1, str2):
    return("".join(['['] + [str1] + [','] + [str2] + [']']))

def snail_mag(arr):
    #arr = eval(instr)
    for i in range(2):
        if not isinstance(arr[i], int):
            arr[i] = snail_mag(arr[i])
            
    #print(arr)
    return(3*arr[0] + 2*arr[1])


# df = '[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]'
# print(snail_reduce(df))


ans = df[0][0]

for i in range(1, len(df), 1):
    ans = snail_add(ans, df[0][i])
    #print(ans)
    ans = snail_reduce(ans)
    #print(ans)

# x = '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
# print(snail_mag(eval(x)))
    
print(f'Answer 1 is {snail_mag(eval(ans))}')

maxmag = 0

for i in range(len(df)-1):
    for j in range(i, len(df)):
        tempmag1 = snail_mag(eval(snail_reduce(snail_add(df[0][i], df[0][j]))))
        if tempmag1 > maxmag:
            maxmag = tempmag1
        
        tempmag2 = snail_mag(eval(snail_reduce(snail_add(df[0][j], df[0][i]))))
        if tempmag2 > maxmag:
            maxmag = tempmag2


print(f'Answer 2 is {maxmag}')
