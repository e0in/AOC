# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 09:00:27 2022

@author: ehorgan
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def marker(s, l=4):
    for i in range(l, len(s)+1):
        if len(set(s[i-l : i])) == l:
            return i
    return 0
        
#print(marker("1234567890"))
assert marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
assert marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert marker("nppdvjthqldpwncqszvftbrmjlhg") == 6
assert marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
assert marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

with open('6.txt', 'r') as file:
    input6 = file.read().rstrip()

print(f'Answer 1 is {marker(input6)}')

assert marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
assert marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
assert marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
assert marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
assert marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26

print(f'Answer 2 is {marker(input6, 14)}')