# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:25:03 2022

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import pytest
import collections


def load_rooms(fname):
    arr = pd.read_csv(fname, sep="[", header=None, names = ["root", "checksum"], engine='python')
    arr['checksum'] = arr['checksum'].str.rstrip(']')
    arr['sid'] = arr['root'].str.split('-').str[-1].astype('int')
    arr['text'] = arr['root'].str.split('-').str[:-1].str.join('')
    #arr.drop('root', axis=1, inplace=True)
    
    arr['common'] = arr['text'].apply(lambda x: collections.Counter(sorted(x)).most_common(5))
    arr['chk'] = arr['common'].apply(lambda x: "".join([c[0] for c in x]))
    arr.drop('common', axis=1, inplace=True)
    arr['valid'] = arr['chk'] == arr['checksum']
    
    return arr, arr.loc[arr['valid'], 'sid'].sum()


[arr, count] = load_rooms("4.txt")

assert load_rooms("4_test.txt")[1] == 1514

print(f'Answer 1 is {count}')


def decode(s, shift):
    ret = []
    for char in s:
        if char == '-':
            ret.append(' ')
        elif char.isnumeric():
            break
        else:
            ret.append(chr( 97 + (ord(char)+shift-97)%26 ))
    return "".join(ret)

assert decode('qzmt-zixmtkozy-ivhz-343', 343) == 'very encrypted name '


arr['name'] = arr.apply(lambda x: decode(x.root, x.sid), axis=1)


print(f"Answer 2 is {arr[arr['name'].str.find('northpole') != -1]['sid'].values[0]}")