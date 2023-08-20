# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:49:29 2021

@author: Eoin
"""

import math
import numpy as np
import pandas as pd
import binascii

with open('16.txt', 'r') as file:
    inputdata = file.read().rstrip()

test = '0123456789'

# Change to True for test data, False for real
data = 16
if data == 1:
    hexstr = 'D2FE28'
elif data == 2:
    hexstr = '38006F45291200'
elif data == 3:
    hexstr = 'EE00D40C823060'
elif data == 4:
    hexstr = '8A004A801A8002F478'
elif data == 5:
    hexstr = '620080001611562C8802118E34'
elif data == 6:
    hexstr = 'C0015000016115A2E0802F182340'
elif data == 7:
    hexstr = 'A0016C880162017C3686B18A3D4780'
elif data == 8:
    hexstr = 'C200B40A82'
elif data == 9:
    hexstr = '04005AC33890'
elif data == 10:
    hexstr = '880086C3E88112'
elif data == 11:
    hexstr = 'CE00C43D881120'
elif data == 12:
    hexstr = 'D8005AC2A8F0'
elif data == 13:
    hexstr = 'F600BC2D8F'
elif data == 14:
    hexstr = '9C005AC2F8F0'
elif data == 15:
    hexstr = '9C0141080250320F1802104A08'
else:
    hexstr = inputdata
    
bin_str = bin(int(hexstr, 16))[2:].zfill(4*len(hexstr))

bit_dig_3 = {"000": 0, "001": 1, "010": 2, "011": 3,
             "100": 4, "101": 5, "110": 6, "111": 7}
deepest_level = 0

class Packet:
    def __init__(self, bin_str, level = 0, length_type_id=None):
        self.version = bit_dig_3[bin_str[0:3]]
        self.typeid = bit_dig_3[bin_str[3:6]]
        self.length_type_id = length_type_id
        self.subpackets = []
        self.literal = None
        self.eval = None
        
        self.level = level
        global deepest_level
        if self.level > deepest_level:
            deepest_level = self.level
        
        self.packet_return = ''
        if self.typeid == 4:
            str_lit = bin_str[6:]
            literal = []
            n=0
            while str_lit[n] == '1':
                literal.append(str_lit[n+1:n+5])
                n += 5
            literal.append(str_lit[n+1:n+5])
            
            self.literal = int("".join(literal), 2)
            self.eval = self.literal
            # print('Created literal packet with value ' + str(self.literal))
            
            if self.length_type_id is not None:
                self.packet_return = str_lit[n+5:]
        else:
            self.length_type_id = bin_str[6]
            if self.length_type_id == '0':
                subs_len = int(bin_str[7:22], 2)
                subpacket_str = bin_str[22:22+subs_len]
                self.packet_return = bin_str[22+subs_len:]
                # print('Creating subpackets length ' + str(subs_len))
                self.subpackets.append(
                    Packet(subpacket_str, level = self.level + 1,
                           length_type_id=bin_str[6]))
                i = 0
                while len(self.subpackets[i].packet_return) > 10:
                    ret_str = self.subpackets[i].packet_return
                    # print('Creating length sub ' + str(len(ret_str)))
                    self.subpackets.append(Packet(ret_str,
                         level = self.level + 1, length_type_id=bin_str[6]))
                    i += 1
                # print('Finished length Subpackets')
            else:
                subs_num = int(bin_str[7:18], 2)
                # print('Creating subpackets, total ' + str(subs_num))
                subpacket_str = bin_str[18:]
                self.subpackets.append(
                    Packet(subpacket_str, level = self.level + 1,
                           length_type_id=bin_str[6]))
                for i in range(subs_num - 1):
                    # print('Creating subpackets, number ' + str(i))
                    self.subpackets.append(Packet(
                        self.subpackets[i].packet_return,
                        level = self.level + 1, length_type_id=bin_str[6]))
                
                self.packet_return = self.subpackets[subs_num-1].packet_return
                # print('Finished number Subpackets')
            
            evals = [subpack.eval for subpack in self.subpackets]
            if self.typeid == 0:
                self.eval = sum(evals)
            elif self.typeid == 1:
                self.eval = math.prod(evals)
            elif self.typeid == 2:
                self.eval = min(evals)
            elif self.typeid == 3:
                self.eval = max(evals)
            elif self.typeid == 5:
                self.eval = int(evals[0] > evals[1])
            elif self.typeid == 6:
                self.eval = int(evals[0] < evals[1])
            elif self.typeid == 7:
                self.eval = int(evals[0] == evals[1])
    
    def version_sum(self):
        total = self.version
        q = self.subpackets
        while q:
            subpack = q.pop()
            total += subpack.version
            
            q += subpack.subpackets
        return(total)        
        
packet = Packet(bin_str)

                    
# print(f'Answer 1 is {packet.version_sum()}')

                    
print(f'Answer 2 is {packet.eval}')
