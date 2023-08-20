# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:47:51 2021

@author: Eoin
"""

test = "1"
input10 = "1113222113"

def lookandsay(str_in, it):
    k = str_in[0]
    n = 0
    
    if len(str_in) == 1:
        str_out = ["1", k]
    else:
        str_out = []
        for i in range(len(str_in)-1):
            if str_in[i] == k:
                n += 1
            else:
                str_out += [str(n), k]
                k = str_in[i]
                n = 1
        
        if k == str_in[-1]:
            n += 1
            str_out += [str(n), k]
        else:
            str_out += [str(n), k]
            str_out += ["1", str_in[-1]]
        
    
    if it == 1:
        return("".join(str_out))
    else:
        return(lookandsay("".join(str_out), it-1))

str1 = lookandsay(input10, 40)

print(f'Answer 1 is {len(str1)}')

str2 = lookandsay(input10, 50)

print(f'Answer 1 is {len(str2)}')