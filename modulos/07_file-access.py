# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:28:20 2019

@author: CEC
"""
devices=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    print(item)
    devices.append(item)
file.close()
print(devices) 

