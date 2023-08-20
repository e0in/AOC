# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 11:35:01 2021

@author: Eoin
"""


import math
import numpy as np
import pandas as pd

hallway = [0, 0, 0, 0, 0, 0, 0]

if True:
    rooms = [[10, 1], [100, 1000], [10, 100], [1000, 1]]
else:
    rooms = [[10, 100], [1, 1000], [10, 1000], [100, 1]]
    
finstate = [[1, 1], [10, 10], [100, 100], [1000, 1000]]
    
minscore = 99999999