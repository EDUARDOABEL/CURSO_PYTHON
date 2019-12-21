# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:42:14 2019

@author: CEC
"""

devices=["R1","R2","R3","S1","S2"]
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
print(switches)        