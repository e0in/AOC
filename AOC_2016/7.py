# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:25:03 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def TLS(ip):
    count = 0
    abba = False
    for i in range(len(ip)-3):
        if ip[i] == '[':
            count += 1
        elif ip[i] == ']':
            count -= 1
        elif ip[i:i+4].isalpha():
            if (ip[i] == ip[i+3]) and (ip[i+1] == ip[i+2]) and (ip[i] != ip[i+1]):
                if count > 0:
                    return False
                else:
                    abba = True
    
    return abba
            
        
assert TLS('abba[mnop]qrst') == True;assert TLS('abcd[bddb]xyyx') == False
assert TLS('aaaa[qwer]tyui') == False;assert TLS('ioxxoj[asdfgh]zxcvbn1') == True

with open('7.txt', 'r') as file:
    addresses = file.read().splitlines()

support = 0
for ip in addresses:
    if TLS(ip):
        support += 1
    
print(f'Answer 1 is {support}')

def SSL(ip):
    count = 0
    aba = set()
    bab = set()
    for i in range(len(ip)-2):
        if ip[i] == '[':
            count += 1
        elif ip[i] == ']':
            count -= 1
        elif ip[i:i+3].isalpha():
            if (ip[i] == ip[i+2]) and (ip[i] != ip[i+1]):
                if count == 0:
                    aba.add((ip[i], ip[i+1]))
                else:
                    bab.add((ip[i+1], ip[i]))
                    
    return len(aba.intersection(bab)) > 0

assert SSL('aba[bab]xyz') == True;assert SSL('xyx[xyx]xyx') == False
assert SSL('aaa[kek]eke') == True;assert SSL('zazbz[bzb]cdb') == True

support2 = 0
for ip in addresses:
    if SSL(ip):
        support2 += 1

print(f'Answer 2 is {support2}')