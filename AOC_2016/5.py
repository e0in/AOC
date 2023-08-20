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
import hashlib


def find_pass(d_id):
    password = []
    i = 0
    
    while len(password) < 8:
        d_hash = d_id + str(i)
        
        if hashlib.md5(d_hash.encode('utf-8')).hexdigest()[:5] == '00000':
            #print(hashlib.md5(d_hash.encode('utf-8')).hexdigest())
            password.append(hashlib.md5(d_hash.encode('utf-8')).hexdigest()[5])
        
        i += 1
    
    return "".join(password)

#assert find_pass('abc') == '18f47a30'

#print(f'Answer 1 is {find_pass("ugkcyxxp")}')

def find_pass_2(d_id):
    password = [None, None, None, None, None, None, None, None]
    i = 0
    
    while None in password:
        d_hash = d_id + str(i)
        
        h = hashlib.md5(d_hash.encode('utf-8')).hexdigest()
        
        if h[:5] == '00000':
            print(h, password)
            if h[5].isnumeric():
                if int(h[5]) < 8:
                    if password[int(h[5])] is None:
                        password[int(h[5])] = h[6]
        
        i += 1
    
    return "".join(password)

#assert find_pass_2('abc') == '05ace8e3'

print(f'Answer 2 is {find_pass_2("ugkcyxxp")}')