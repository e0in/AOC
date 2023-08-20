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

if True:
    elem = ['H', 'L']
    micro = [['H', 'L'], [], [], []]
    gen = [[], ['H'], ['L'], []]
else:
    elem = ['T', 'U', 'S', 'P', 'R'] # thulium, plutonium, strontium, promethium, ruthenium
    micro = [['T'], ['U', 'S'], ['P', 'R'], []]
    gen = [['T', 'U', 'S'], [], ['P', 'R'], []]

elev = 0
steps = 0
    
    
# The first floor contains a thulium generator, a thulium-compatible microchip,
# a plutonium generator, and a strontium generator.
    
# The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.

# The third floor contains a promethium generator, a promethium-compatible microchip,
# a ruthenium generator, and a ruthenium-compatible microchip.

# The fourth floor contains nothing relevant.

        
    
# print(f'Answer 1 is {}')


# print(f'Answer 2 is {}')